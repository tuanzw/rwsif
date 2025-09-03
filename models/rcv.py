from pydantic import BaseModel, Field, field_validator
from typing import Annotated, Optional
from datetime import datetime
import re

class RCV(BaseModel):
    Record_Type: Annotated[str, Field(max_length=3, min_length=3)]
    Merge_Action: Annotated[str, Field(max_length=1, min_length=1)]
    Line_Id: Optional[Annotated[int, Field(ge=0, le=999999)]] = None
    Location_Id: Annotated[str, Field(max_length=20)]
    Site_Id: Annotated[str, Field(max_length=10)]
    Sku_Id: Annotated[str, Field(max_length=50)]
    Tag_Id: Optional[Annotated[str, Field(max_length=20)]] = None
    Qty_On_Hand: Annotated[float, Field(ge=-999999999.999999, le=999999999.999999)]
    Supplier_Id: Optional[Annotated[str, Field(max_length=15)]] = None
    Batch_Id: Optional[Annotated[str, Field(max_length=15)]] = None
    Expiry_Dstamp: Optional[Annotated[str, Field(max_length=14, min_length=14)]] = None
    Config_Id: Optional[Annotated[str, Field(max_length=15)]] = None
    Receipt_Id: Optional[Annotated[str, Field(max_length=20)]] = None
    Condition_Id: Optional[Annotated[str, Field(max_length=10)]] = None
    Tag_Copies: Optional[Annotated[int, Field(ge=0, le=99)]] = None
    Receipt_Dstamp: Optional[Annotated[str, Field(max_length=14, min_length=14)]] = None
    Lock_Code: Optional[Annotated[str, Field(max_length=10)]] = None
    Notes: Optional[Annotated[str, Field(max_length=80)]] = None
    Pallet_Id: Optional[Annotated[str, Field(max_length=20)]] = None
    Pallet_Config: Optional[Annotated[str, Field(max_length=15)]] = None
    Pallet_Volume: Optional[Annotated[float, Field(ge=-9999999.999999, le=9999999.999999)]] = None
    Pallet_Height: Optional[Annotated[float, Field(ge=-999999999.999999, le=999999999.999999)]] = None
    Pallet_Depth: Optional[Annotated[float, Field(ge=-9999.999, le=9999.999)]] = None
    Pallet_Width: Optional[Annotated[float, Field(ge=-9999.999, le=9999.999)]] = None
    Pallet_Weight: Optional[Annotated[float, Field(ge=-9999999.999999, le=9999999.999999)]] = None
    Pallet_Grouped: Optional[Annotated[str, Field(max_length=1)]] = None
    Owner_Id: Annotated[str, Field(max_length=10)]
    Origin_Id: Optional[Annotated[str, Field(max_length=10)]] = None
    Manuf_Dstamp: Optional[Annotated[str, Field(max_length=14, min_length=14)]] = None
    Sampling_Type: Optional[Annotated[str, Field(max_length=20)]] = None
    Client_Id: Annotated[str, Field(max_length=10)]
    User_Def_Type_1: Optional[Annotated[str, Field(max_length=30)]] = None
    User_Def_Type_2: Optional[Annotated[str, Field(max_length=30)]] = None
    User_Def_Type_3: Optional[Annotated[str, Field(max_length=30)]] = None
    User_Def_Type_4: Optional[Annotated[str, Field(max_length=30)]] = None
    User_Def_Type_5: Optional[Annotated[str, Field(max_length=30)]] = None
    User_Def_Type_6: Optional[Annotated[str, Field(max_length=30)]] = None
    User_Def_Type_7: Optional[Annotated[str, Field(max_length=30)]] = None
    User_Def_Type_8: Optional[Annotated[str, Field(max_length=30)]] = None
    User_Def_Chk_1: Optional[Annotated[str, Field(max_length=1)]] = None
    User_Def_Chk_2: Optional[Annotated[str, Field(max_length=1)]] = None
    User_Def_Chk_3: Optional[Annotated[str, Field(max_length=1)]] = None
    User_Def_Chk_4: Optional[Annotated[str, Field(max_length=1)]] = None
    User_Def_Date_1: Optional[Annotated[str, Field(max_length=14, min_length=14)]] = None
    User_Def_Date_2: Optional[Annotated[str, Field(max_length=14, min_length=14)]] = None
    User_Def_Date_3: Optional[Annotated[str, Field(max_length=14, min_length=14)]] = None
    User_Def_Date_4: Optional[Annotated[str, Field(max_length=14, min_length=14)]] = None
    User_Def_Num_1: Optional[Annotated[float, Field(ge=-999999999.999999, le=999999999.999999)]] = None
    User_Def_Num_2: Optional[Annotated[float, Field(ge=-999999999.999999, le=999999999.999999)]] = None
    User_Def_Num_3: Optional[Annotated[float, Field(ge=-999999999.999999, le=999999999.999999)]] = None
    User_Def_Num_4: Optional[Annotated[float, Field(ge=-999999999.999999, le=999999999.999999)]] = None
    User_Def_Note_1: Optional[Annotated[str, Field(max_length=200)]] = None
    User_Def_Note_2: Optional[Annotated[str, Field(max_length=200)]] = None
    Time_Zone_Name: Optional[Annotated[str, Field(max_length=64)]] = None
    Client_Group: Optional[Annotated[str, Field(max_length=10)]] = None
    Tracking_Level: Optional[Annotated[str, Field(max_length=8)]] = None
    Ce_Consignment_Id: Optional[Annotated[str, Field(max_length=18)]] = None
    Ce_Receipt_Type: Optional[Annotated[str, Field(max_length=2)]] = None
    Ce_Originator: Optional[Annotated[str, Field(max_length=25)]] = None
    Ce_Originator_Ref: Optional[Annotated[str, Field(max_length=25)]] = None
    Ce_Coo: Optional[Annotated[str, Field(max_length=3)]] = None
    Ce_Cwc: Optional[Annotated[str, Field(max_length=3)]] = None
    Ce_Ucr: Optional[Annotated[str, Field(max_length=20)]] = None
    Ce_Under_Bond: Optional[Annotated[str, Field(max_length=1)]] = None
    Ce_Document_Dstamp: Optional[Annotated[str, Field(max_length=14, min_length=14)]] = None
    Spec_Code: Optional[Annotated[str, Field(max_length=99)]] = None
    Ce_Duty_Stamp: Optional[Annotated[str, Field(max_length=1)]] = None
    Nls_Calendar: Optional[Annotated[str, Field(max_length=30)]] = None

    model_config = {
        "str_strip_whitespace": True,
        "extra": "forbid"
    }

    # Validator for Record_Type
    @field_validator("Record_Type")
    @classmethod
    def record_type_must_be_rcv(cls, v: str) -> str:
        if v != "RCV":
            raise ValueError("Record_Type must be 'RCV'")
        return v

    # Validator for Merge_Action
    @field_validator("Merge_Action")
    @classmethod
    def merge_action_allowed_values(cls, v: str) -> str:
        if v != "A":
            raise ValueError("Merge_Action must be 'A'")
        return v

    # Validator for Y/N flags
    @field_validator("Pallet_Grouped", "User_Def_Chk_1", "User_Def_Chk_2", "User_Def_Chk_3", "User_Def_Chk_4", "Ce_Under_Bond", "Ce_Duty_Stamp")
    @classmethod
    def y_n_flags(cls, v: Optional[str], info) -> Optional[str]:
        if v is not None and v not in ["Y", "N"]:
            raise ValueError(f"{info.field_name} must be 'Y' or 'N'")
        return v

    # Uppercase validation for required and optional string fields
    @field_validator(
        "Location_Id", "Site_Id", "Sku_Id", "Tag_Id", "Supplier_Id", "Batch_Id", 
        "Config_Id", "Receipt_Id", "Condition_Id", "Lock_Code", "Pallet_Id", 
        "Pallet_Config", "Owner_Id", "Origin_Id", "Sampling_Type", "Client_Id",
        "User_Def_Type_1", "User_Def_Type_2", "User_Def_Type_3", "User_Def_Type_4",
        "User_Def_Type_5", "User_Def_Type_6", "User_Def_Type_7", "User_Def_Type_8",
        "Client_Group", "Tracking_Level", "Ce_Consignment_Id", "Ce_Receipt_Type",
        "Ce_Originator", "Ce_Originator_Ref", "Ce_Coo", "Ce_Cwc", "Ce_Ucr", "Spec_Code"
    )
    @classmethod
    def enforce_uppercase(cls, v: Optional[str], info) -> Optional[str]:
        if v is not None and v != '' and not v.isupper():
            v = v.upper()
        return v

    # Date format validation (YYYYMMDDHH24MISS)
    @field_validator(
        "Expiry_Dstamp", "Receipt_Dstamp", "Manuf_Dstamp", 
        "User_Def_Date_1", "User_Def_Date_2", "User_Def_Date_3", "User_Def_Date_4",
        "Ce_Document_Dstamp"
    )
    @classmethod
    def validate_date_format(cls, v: Optional[str], info) -> Optional[str]:
        if v is not None:
            try:
                datetime.strptime(v, "%Y%m%d%H%M%S")
            except ValueError:
                raise ValueError(f"{info.field_name} must be in format 'YYYYMMDDHH24MISS'")
        return v

    # Decimal precision validation (6 decimal places for specified fields)
    @field_validator("Qty_On_Hand", "Pallet_Volume", "Pallet_Height", "User_Def_Num_1", "User_Def_Num_2", "User_Def_Num_3", "User_Def_Num_4")
    @classmethod
    def validate_six_decimal_precision(cls, v: Optional[float], info) -> Optional[float]:
        if v is not None:
            if not re.match(r"^-?\d{1,9}(\.\d{0,6})?$", str(v)):
                raise ValueError(f"{info.field_name} must have up to 6 decimal places and max 9 integer digits")
        return v

    # Decimal precision validation (3 decimal places for Pallet_Depth and Pallet_Width)
    @field_validator("Pallet_Depth", "Pallet_Width")
    @classmethod
    def validate_three_decimal_precision(cls, v: Optional[float], info) -> Optional[float]:
        if v is not None:
            if not re.match(r"^-?\d{1,4}(\.\d{0,3})?$", str(v)):
                raise ValueError(f"{info.field_name} must have up to 3 decimal places and max 4 integer digits")
        return v

    # Decimal precision validation (6 decimal places for Pallet_Weight)
    @field_validator("Pallet_Weight")
    @classmethod
    def validate_weight_decimal_precision(cls, v: Optional[float], info) -> Optional[float]:
        if v is not None:
            if not re.match(r"^-?\d{1,7}(\.\d{0,6})?$", str(v)):
                raise ValueError(f"{info.field_name} must have up to 6 decimal places and max 7 integer digits")
        return v

# Example Usage
if __name__ == "__main__":
    valid_data = {
        "Record_Type": "RCV",
        "Merge_Action": "A",
        "Line_Id": 123456,
        "Location_Id": "LOC123",
        "Site_Id": "SITE123",
        "Sku_Id": "SKU12345",
        "Tag_Id": "TAG123",
        "Qty_On_Hand": 123456.789012,
        "Supplier_Id": "SUP123",
        "Batch_Id": "BATCH123",
        "Expiry_Dstamp": "20250903102600",
        "Config_Id": "CONFIG001",
        "Receipt_Id": "REC123",
        "Condition_Id": "COND123",
        "Tag_Copies": 10,
        "Receipt_Dstamp": "20250903102600",
        "Lock_Code": "LOCK123",
        "Notes": "Sample note",
        "Pallet_Id": "PAL123",
        "Pallet_Config": "PCONFIG123",
        "Pallet_Volume": 1234.567890,
        "Pallet_Height": 123456.789012,
        "Pallet_Depth": 123.456,
        "Pallet_Width": 123.456,
        "Pallet_Weight": 1234.567890,
        "Pallet_Grouped": "Y",
        "Owner_Id": "OWN123",
        "Origin_Id": "ORIG123",
        "Manuf_Dstamp": "20250903102600",
        "Sampling_Type": "SAMPLE123",
        "Client_Id": "CLIENT123",
        "User_Def_Type_1": "TYPE1",
        "User_Def_Chk_1": "Y",
        "User_Def_Date_1": "20250903102600",
        "User_Def_Num_1": 123456.789012,
        "User_Def_Note_1": "Note 1",
        "Time_Zone_Name": "America/New_York",
        "Client_Group": "GROUP123",
        "Tracking_Level": "TRACK123",
        "Ce_Consignment_Id": "CONS123",
        "Ce_Receipt_Type": "RT",
        "Ce_Originator": "ORIGIN123",
        "Ce_Originator_Ref": "REF123",
        "Ce_Coo": "COO",
        "Ce_Cwc": "CWC",
        "Ce_Ucr": "UCR123",
        "Ce_Under_Bond": "N",
        "Ce_Document_Dstamp": "20250903102600",
        "Spec_Code": "SPEC123",
        "Ce_Duty_Stamp": "N",
        "Nls_Calendar": "CAL123"
    }

    try:
        rcv = RCV(**valid_data)
        print("Valid data:", rcv.model_dump())
    except ValueError as e:
        print("Validation error:", str(e))