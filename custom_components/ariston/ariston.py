"""Ariston API"""
from __future__ import annotations

import aiohttp
import logging

from typing import Any, final
from datetime import date
from enum import IntFlag, unique

ARISTON_API_URL: final = "https://www.ariston-net.remotethermo.com/api/v2/"
ARISTON_LOGIN: final = "accounts/login"
ARISTON_REMOTE: final = "remote"
ARISTON_PLANTS: final = "plants"
ARISTON_LITE: final = "lite"
ARISTON_DATA_ITEMS: final = "dataItems"
ARISTON_ZONES: final = "zones"
ARISTON_PLANT_DATA: final = "plantData"
ARISTON_REPORTS: final = "reports"
ARISTON_TIME_PROGS: final = "timeProgs"

_LOGGER = logging.getLogger(__name__)


@unique
class PlantMode(IntFlag):
    """Plant mode enum"""

    UNDEFINED = -1
    SUMMER = 0
    WINTER = 1
    HEATING_ONLY = 2
    COOLING = 3
    COOLING_ONLY = 4
    OFF = 5


@unique
class ZoneMode(IntFlag):
    """Zone mode enum"""

    UNDEFINED = -1
    OFF = 0
    MANUAL = 1
    MANUAL2 = 2
    TIME_PROGRAM = 3


@unique
class DhwMode(IntFlag):
    """Dhw mode enum"""

    DISABLED = 0
    TIME_BASED = 1
    ALWAYS_ACTIVE = 2
    HC_HP = 3
    HC_HP_40 = 4
    GREEN = 5


@unique
class Weather(IntFlag):
    """Weather enum"""

    UNAVAILABLE = 0
    CLEAR = 1
    VARIABLE = 2
    CLOUDY = 3
    RAINY = 4
    RAINSTORM = 5
    SNOW = 6
    FOG = 7
    WINDY = 8
    CLEAR_BY_NIGHT = 129
    VARIABLE_BY_NIGHT = 130


@unique
class GasEnergyUnit(IntFlag):
    """Gas energy unit enum"""

    KWH = 0
    GIGA_JOULE = 1
    THERM = 2
    MEGA_BTU = 3
    SMC = 4
    CUBE_METER = 5


@unique
class GasType(IntFlag):
    """Gas type enu,"""

    NATURAL_GAS = 0
    LPG = 1
    AIR_PROPANED = 2
    GPO = 3
    PROPANE = 4


@unique
class Currency(IntFlag):
    """Currency enum"""

    ARS = 1
    EUR = 2
    BYN = 3
    CNY = 4
    HRK = 5
    CZK = 6
    DKK = 7
    HKD = 8
    HUF = 9
    IRR = 10
    KZT = 11
    CHF = 12
    MOP = 13
    PLZ = 14
    RON = 15
    RUB = 16
    TRY = 17
    UAH = 18
    GBP = 19
    USD = 20


class DeviceAttribute:
    """Constants for device attributes"""

    GW_FW_VER: final = "gwFwVer"
    GW_ID: final = "gwId"
    GW_LINK: final = "gwLink"
    GW_SERIAL: final = "gwSerial"
    GW_SYS_TYPE: final = "gwSysType"
    PLANT_NAME: final = "plantName"


class ZoneAttribute:
    """Constants for zone attributes"""

    NUM: final = "num"
    NAME: final = "name"
    ROOM_SENS: final = "roomSens"
    GEOFENCE_DEROGA: final = "geofenceDeroga"


class DeviceFeatures:
    """Constants for device features"""

    AUTO_THERMO_REG: final = "autoThermoReg"
    BMS_ACTIVE: final = "bmsActive"
    BUFFER_TIME_PROG_AVAILABLE: final = "bufferTimeProgAvailable"
    CASCDE_SYS: final = "cascadeSys"
    CONV_BOILER: final = "convBoiler"
    DHW_BOILER_PRESENT: final = "dhwBoilerPresent"
    DHW_HIDDEN: final = "dhwHidden"
    DHW_MODE_CHANGEABLE: final = "dhwModeChangeable"
    DHW_PROG_SUPPORTED: final = "dhwProgSupported"
    DICTINCT_HEAT_COOL_SETPOINT: final = "distinctHeatCoolSetpoints"
    EXTENDED_TIME_PROG: final = "extendedTimeProg"
    HAS_BOILER: final = "hasBoiler"
    HAS_EM20: final = "hasEm20"
    HAS_FIREPLACE: final = "hasFireplace"
    HAS_METERING: final = "hasMetering"
    HAS_SLP: final = "hasSlp"
    HAS_TWO_COOLING_TEMP: final = "hasTwoCoolingTemp"
    HAS_VMC: final = "hasVmc"
    HAS_ZONE_NAMES: final = "hasZoneNames"
    HP_CASCADE_CONFIG: final = "hpCascadeConfig"
    HP_CASCADE_SYS: final = "hpCascadeSys"
    HP_SYS: final = "hpSys"
    HV_INPUT_OFF: final = "hvInputOff"
    HYBRID_SYS: final = "hybridSys"
    IS_EVO2: final = "isEvo2"
    IS_VMC_R2: final = "isVmcR2"
    PILOT_SUPPORTED: final = "pilotSupported"
    PRE_HEATING_SUPPORTED: final = "preHeatingSupported"
    SOLAR: final = "solar"
    VIRTUAL_ZONES: final = "virtualZones"
    ZONES: final = "zones"
    WEATHER_PROVIDER: final = "weatherProvider"


class DeviceProperties:
    """Constants for device properties"""

    PLANT_MODE: final = "PlantMode"
    IS_FLAME_ON: final = "IsFlameOn"
    HOLIDAY: final = "Holiday"
    OUTSIDE_TEMP: final = "OutsideTemp"
    HEATING_CIRCUIT_PRESSURE: final = "HeatingCircuitPressure"
    CH_FLOW_SETPOINT_TEMP: final = "ChFlowSetpointTemp"
    DHW_TEMP: final = "DhwTemp"
    DHW_MODE: final = "DhwMode"
    AUTOMATIC_THERMOREGULATION: final = "AutomaticThermoregulation"
    ANTILEGIONELLA_ON_OFF: final = "AntilegionellaOnOff"
    ANTILEGIONELLA_TEMP: final = "AntilegionellaTemp"
    ANTILEGIONELLA_FREQ: final = "AntilegionellaFreq"


class ThermostatProperties:
    """Constants for thermostat properties"""

    ZONE_MEASURED_TEMP: final = "ZoneMeasuredTemp"
    ZONE_DESIRED_TEMP: final = "ZoneDesiredTemp"
    ZONE_COMFORT_TEMP: final = "ZoneComfortTemp"
    ZONE_MODE: final = "ZoneMode"
    ZONE_HEAT_REQUEST: final = "ZoneHeatRequest"
    ZONE_ECONOMY_TEMP: final = "ZoneEconomyTemp"
    ZONE_DEROGA: final = "ZoneDeroga"


class ConsumptionProperties:
    """Constants for consumption properties"""

    CURRENCY: final = "currency"
    GAS_TYPE: final = "gasType"
    GAS_ENERGY_UNIT: final = "gasEnergyUnit"
    ELEC_COST: final = "elecCost"
    GAS_COST: final = "gasCost"


class PropertyType:
    """Constants for property types"""

    VALUE: final = "value"
    OPTIONS: final = "options"
    OPT_TEXTS: final = "optTexts"
    UNIT: final = "unit"
    MIN: final = "min"
    MAX: final = "max"
    STEP: final = "step"
    DECIMALS: final = "decimals"
    ZONE: final = "zone"
    EXPIRES_ON: final = "expiresOn"


class AristonAPI:
    """Ariston API class"""

    def __init__(self, username: str, password: str) -> None:
        """Constructor for Ariston API."""
        self.__username = username
        self.__password = password
        self.__token = ""

    async def async_connect(self) -> bool:
        """Login to ariston cloud and get token"""

        response = await self.post(
            f"{ARISTON_API_URL}{ARISTON_LOGIN}",
            {"usr": self.__username, "pwd": self.__password},
        )

        if response is None:
            return False

        self.__token = response["token"]

        return True

    async def async_get_detailed_devices(self) -> dict[str, Any]:
        """Get detailed cloud devices"""
        return await self.get(f"{ARISTON_API_URL}{ARISTON_REMOTE}/{ARISTON_PLANTS}")

    async def async_get_devices(self) -> dict[str, Any]:
        """Get cloud devices"""
        return await self.get(
            f"{ARISTON_API_URL}{ARISTON_REMOTE}/{ARISTON_PLANTS}/{ARISTON_LITE}"
        )

    async def async_get_features_for_device(self, gw_id: str) -> dict[str, Any]:
        """Get features for the device"""
        return await self.get(
            f"{ARISTON_API_URL}{ARISTON_REMOTE}/{ARISTON_PLANTS}/{gw_id}/features"
        )

    async def async_get_energy_account(self, gw_id: str) -> dict[str, Any]:
        """Get energy account for the device"""
        return await self.get(
            f"{ARISTON_API_URL}{ARISTON_REMOTE}/{ARISTON_REPORTS}/{gw_id}/energyAccount"
        )

    async def async_get_consumptions_sequences(
        self, gw_id: str, has_boiler: bool, has_slp: bool
    ) -> dict[str, Any]:
        """Get consumption sequences for the device"""
        return await self.get(
            f"{ARISTON_API_URL}{ARISTON_REMOTE}/{ARISTON_REPORTS}/{gw_id}/consSequencesApi8?usages=Ch{'%2CDhw' if has_boiler else ''}&hasSlp={has_slp}"
        )

    async def async_get_consumptions_settings(self, gw_id: str) -> dict[str, Any]:
        """Get consumption settings"""
        return await self.post(
            f"{ARISTON_API_URL}{ARISTON_REMOTE}/{ARISTON_PLANTS}/{gw_id}/getConsumptionsSettings",
            {},
        )

    async def async_set_consumptions_settings(
        self,
        gw_id: str,
        consumptions_settings,
    ) -> dict[str, Any]:
        """Get consumption settings"""
        return await self.post(
            f"{ARISTON_API_URL}{ARISTON_REMOTE}/{ARISTON_PLANTS}/{gw_id}/consumptionsSettings",
            consumptions_settings,
        )

    @staticmethod
    def get_items(features: dict[str, Any]):
        """Get the final strings from DeviceProperies and ThermostatProperties"""
        device_props = [
            getattr(DeviceProperties, device_property)
            for device_property in dir(DeviceProperties)
            if not device_property.startswith("__")
        ]
        thermostat_props = [
            getattr(ThermostatProperties, thermostat_properties)
            for thermostat_properties in dir(ThermostatProperties)
            if not thermostat_properties.startswith("__")
        ]

        items = []
        for device_prop in device_props:
            items.append({"id": device_prop, "zn": 0})

        for zone in features[DeviceFeatures.ZONES]:
            for thermostat_prop in thermostat_props:
                items.append({"id": thermostat_prop, "zn": zone[ZoneAttribute.NUM]})
        return items

    async def async_get_properties(
        self, gw_id: str, features: dict[str, Any], culture: str, umsys: str
    ) -> dict[str, Any]:
        """Get device properties"""

        return await self.post(
            f"{ARISTON_API_URL}{ARISTON_REMOTE}/{ARISTON_DATA_ITEMS}/{gw_id}/get?umsys={umsys}",
            {
                "items": self.get_items(features),
                "features": features,
                "culture": culture,
            },
        )

    async def async_set_property(
        self,
        gw_id: str,
        zone_id: int,
        features: dict[str, Any],
        device_property: str,
        value: float,
        prev_value: float,
        umsys: str,
    ) -> dict[str, Any]:
        """Set device properties"""
        return await self.post(
            f"{ARISTON_API_URL}{ARISTON_REMOTE}/{ARISTON_DATA_ITEMS}/{gw_id}/set?umsys={umsys}",
            {
                "items": [
                    {
                        "id": device_property,
                        "prevValue": prev_value,
                        "value": value,
                        "zone": zone_id,
                    }
                ],
                "features": features,
            },
        )

    async def async_get_thermostat_time_progs(
        self, gw_id: str, zone: int, umsys: str
    ) -> dict[str, Any]:
        """Get thermostat time programs"""
        return await self.get(
            f"{ARISTON_API_URL}{ARISTON_REMOTE}/{ARISTON_TIME_PROGS}/{gw_id}/ChZn{zone}?umsys={umsys}",
        )

    async def async_set_holiday(
        self,
        gw_id: str,
        holiday_end_date: date,
    ) -> None:
        """Set holidays"""

        await self.post(
            f"{ARISTON_API_URL}{ARISTON_REMOTE}/{ARISTON_PLANT_DATA}/{gw_id}/holiday",
            {
                "new": holiday_end_date,
            },
        )

    async def __request(
        self,
        method: str,
        path: str,
        params: dict[str, Any] = None,
        body: dict[str, Any] = None,
        is_retry: bool = False,
    ) -> dict[str, Any]:
        headers = {"ar.authToken": self.__token}

        _LOGGER.debug(
            "Request method %s, path: %s, params: %s, body: %s",
            method,
            path,
            params,
            body,
        )

        async with aiohttp.ClientSession() as session:
            response = await session.request(
                method, path, params=params, json=body, headers=headers
            )

            if not response.ok:
                if response.status == 405:
                    if not is_retry:
                        if await self.async_connect():
                            return await self.__request(
                                method, path, params, body, True
                            )
                        raise Exception("Login failed (password changed?)")
                    raise Exception("Invalid token")
                if response.status == 404:
                    return None
                raise Exception(response.status)

            if response.content_length > 0:
                json = await response.json()
                _LOGGER.debug("Response %s", json)
                return json

            return None

    async def post(self, path: str, body: dict[str, Any] = None) -> dict[str, Any]:
        """POST request"""
        return await self.__request("POST", path, None, body)

    async def get(self, path: str, params: dict[str, Any] = None) -> dict[str, Any]:
        """GET request"""
        return await self.__request("GET", path, params, None)
