"""Support for Ariston switches."""
from __future__ import annotations

import logging

from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.components.switch import SwitchEntity

from .entity import AristonEntity
from .ariston import DeviceAttribute, PropertyType
from .const import ARISTON_SWITCH_TYPES, DOMAIN, AristonSwitchEntityDescription
from .coordinator import DeviceDataUpdateCoordinator, DeviceEnergyUpdateCoordinator


_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry, async_add_entities
) -> None:
    """Set up the Ariston switches from config entry."""
    ariston_switches: list[AristonSwitch] = []
    for description in ARISTON_SWITCH_TYPES:
        coordinator: DeviceDataUpdateCoordinator or DeviceEnergyUpdateCoordinator = (
            hass.data[DOMAIN][entry.unique_id][description.coordinator]
        )
        if coordinator.device.are_device_features_available(
            description.device_features, description.extra_energy_feature
        ):
            ariston_switches.append(
                AristonSwitch(
                    coordinator,
                    description,
                )
            )

    async_add_entities(ariston_switches)


class AristonSwitch(AristonEntity, SwitchEntity):
    """Base class for specific ariston switches"""

    def __init__(
        self,
        coordinator: DeviceDataUpdateCoordinator or DeviceEnergyUpdateCoordinator,
        description: AristonSwitchEntityDescription,
    ) -> None:
        """Initialize the switch."""
        super().__init__(coordinator, description)

    @property
    def unique_id(self):
        """Return the unique id."""
        return (
            f"{self.coordinator.device.attributes[DeviceAttribute.GW_ID]}-{self.name}"
        )

    @property
    def is_on(self):
        """Return true if switch is on."""
        return self.coordinator.device.get_item_by_id(
            self.entity_description.key, PropertyType.VALUE
        )

    async def async_turn_on(self, **kwargs) -> None:
        """Turn the switch on."""
        await self.coordinator.device.async_set_item_by_id(
            self.entity_description.key, 1.0
        )
        self.async_write_ha_state()

    async def async_turn_off(self, **kwargs) -> None:
        """Turn the device off."""
        await self.coordinator.device.async_set_item_by_id(
            self.entity_description.key, 0.0
        )
        self.async_write_ha_state()
