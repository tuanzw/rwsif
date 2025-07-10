from pydantic import BaseModel, Field, field_validator
from typing import Annotated, Optional
from datetime import datetime

class SSC(BaseModel):
    Record_Type: Annotated[str, Field(max_length=3, min_length=3)]
    Merge_Action: Annotated[str, Field(max_length=1, min_length=1)]
    Sku_Id: Annotated[str, Field(max_length=50)]
    Config_Id: Annotated[str, Field(max_length=15)]
    Main_Config_Id: Annotated[str, Field(max_length=1)] = 'N'
    Client_Id: Annotated[str, Field(max_length=10)]
    Min_Full_Pallet_Perc: Optional[Annotated[int, Field(ge=0, le=999)]] = None
    Max_Full_Pallet_Perc: Optional[Annotated[int, Field(ge=0, le=999)]] = None
    Time_Zone_Name: Optional[Annotated[str, Field(max_length=64)]] = None
    Collective_Mode: Annotated[str, Field(max_length=1)] = 'N'
    Nls_Calendar: Optional[Annotated[str, Field(max_length=30)]] = None
    Collective_Sequence: Optional[Annotated[int, Field(ge=0, le=9999999999)]] = None
    Disabled: Annotated[str, Field(max_length=1)] = 'N'

    model_config = {
        "str_strip_whitespace": True,
        "extra": "forbid"
    }

    # Validators for Allowed Values
    @field_validator("Record_Type")
    @classmethod
    def record_type_must_be_ssc(cls, v: str) -> str:
        if v != "SSC":
            raise ValueError("Record_Type must be 'SSC'")
        return v

    @field_validator("Merge_Action")
    @classmethod
    def merge_action_allowed_values(cls, v: str) -> str:
        if v not in ["A", "U", "D"]:
            raise ValueError("Merge_Action must be 'A', 'U', or 'D'")
        return v

    @field_validator("Main_Config_Id", "Collective_Mode", "Disabled")
    @classmethod
    def y_n_flags(cls, v: str, info) -> str:
        if v not in ["Y", "N"]:
            raise ValueError(f"{info.field_name} must be 'Y' or 'N'")
        return v

    # Uppercase Validation
    @field_validator("Sku_Id", "Config_Id", "Client_Id")
    @classmethod
    def enforce_uppercase(cls, v: str, info) -> str:
        if v != '' and not v.isupper():
            v = v.upper()
        return v

    # Percentage Validation
    @field_validator("Min_Full_Pallet_Perc", "Max_Full_Pallet_Perc")
    @classmethod
    def validate_percentage(cls, v: Optional[int], info) -> Optional[int]:
        if v is not None and (v < 0 or v > 100):
            raise ValueError(f"{info.field_name} must be between 0 and 100")
        return v

# Example Usage
if __name__ == "__main__":
    valid_data = {
        "Record_Type": "SSC",
        "Merge_Action": "A",
        "Sku_Id": "SKU12345",
        "Config_Id": "CONFIG001",
        "Client_Id": "CLIENT1",
        "Main_Config_Id": "N",
        "Min_Full_Pallet_Perc": 80,
        "Collective_Mode": "N"
    }

    try:
        ssc = SSC(**valid_data)
        print("Valid data:", ssc.model_dump())
    except ValueError as e:
        print("Validation error:", str(e))