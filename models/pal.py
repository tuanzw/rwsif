from pydantic import BaseModel, Field, field_validator
from typing import Annotated, Optional
from datetime import datetime

class PAL(BaseModel):
    Record_Type: Annotated[str, Field(max_length=3, min_length=3)]
    Merge_Action: Annotated[str, Field(max_length=1, min_length=1)]
    Pre_Advice_Id: Annotated[str, Field(max_length=20)]
    Line_Id: Optional[Annotated[int, Field(le=999999)]] = None
    Sku_Id: Annotated[str, Field(max_length=50)]
    Config_Id: Optional[Annotated[str, Field(max_length=15)]] = None
    Batch_Id: Optional[Annotated[str, Field(max_length=20)]] = None
    Expiry_Dstamp: Optional[Annotated[str, Field(max_length=14, min_length=14)]] = None
    Pallet_Config: Optional[Annotated[str, Field(max_length=15)]] = None
    Condition_Id: Optional[Annotated[str, Field(max_length=10)]] = None
    Qty_Due: Annotated[float, Field(le=999999999999999)]
    Lock_Code: Optional[Annotated[str, Field(max_length=10)]] = None
    Tag_Id: Optional[Annotated[str, Field(max_length=20)]] = None
    Origin_Id: Optional[Annotated[str, Field(max_length=10)]] = None
    Notes: Optional[Annotated[str, Field(max_length=80)]] = None
    Manuf_Dstamp: Optional[Annotated[str, Field(max_length=14, min_length=14)]] = None
    Client_Id: Annotated[str, Field(max_length=10)]
    Disallow_Merge_Rules: Optional[Annotated[str, Field(max_length=1, min_length=1)]] = None
    User_Def_Type_1: Optional[Annotated[str, Field(max_length=30)]] = None
    User_Def_Type_2: Optional[Annotated[str, Field(max_length=30)]] = None
    User_Def_Type_3: Optional[Annotated[str, Field(max_length=30)]] = None
    User_Def_Type_4: Optional[Annotated[str, Field(max_length=30)]] = None
    User_Def_Type_5: Optional[Annotated[str, Field(max_length=30)]] = None
    User_Def_Type_6: Optional[Annotated[str, Field(max_length=30)]] = None
    User_Def_Type_7: Optional[Annotated[str, Field(max_length=30)]] = None
    User_Def_Type_8: Optional[Annotated[str, Field(max_length=30)]] = None
    User_Def_Chk_1: Optional[Annotated[str, Field(max_length=1, min_length=1)]] = None
    User_Def_Chk_2: Optional[Annotated[str, Field(max_length=1, min_length=1)]] = None
    User_Def_Chk_3: Optional[Annotated[str, Field(max_length=1, min_length=1)]] = None
    User_Def_Chk_4: Optional[Annotated[str, Field(max_length=1, min_length=1)]] = None
    User_Def_Date_1: Optional[Annotated[str, Field(max_length=14, min_length=14)]] = None
    User_Def_Date_2: Optional[Annotated[str, Field(max_length=14, min_length=14)]] = None
    User_Def_Date_3: Optional[Annotated[str, Field(max_length=14, min_length=14)]] = None
    User_Def_Date_4: Optional[Annotated[str, Field(max_length=14, min_length=14)]] = None
    User_Def_Num_1: Optional[Annotated[float, Field(le=999999999999999)]] = None
    User_Def_Num_2: Optional[Annotated[float, Field(le=999999999999999)]] = None
    User_Def_Num_3: Optional[Annotated[float, Field(le=999999999999999)]] = None
    User_Def_Num_4: Optional[Annotated[float, Field(le=999999999999999)]] = None
    User_Def_Note_1: Optional[Annotated[str, Field(max_length=200)]] = None
    User_Def_Note_2: Optional[Annotated[str, Field(max_length=200)]] = None
    Time_Zone_Name: Optional[Annotated[str, Field(max_length=64)]] = None
    Spec_Code: Optional[Annotated[str, Field(max_length=99)]] = None
    Client_Group: Optional[Annotated[str, Field(max_length=10)]] = None
    Tracking_Level: Optional[Annotated[str, Field(max_length=8)]] = None
    Host_Pre_Advice_Id: Optional[Annotated[str, Field(max_length=20)]] = None
    Host_Line_Id: Optional[Annotated[str, Field(max_length=20)]] = None
    Qty_Due_Tolerance: Optional[Annotated[float, Field(le=999999)]] = None
    Ce_Coo: Optional[Annotated[str, Field(max_length=3)]] = None
    Owner_Id: Optional[Annotated[str, Field(max_length=10)]] = None
    Ce_Consignment_Id: Optional[Annotated[str, Field(max_length=18)]] = None
    Collective_Mode: Optional[Annotated[str, Field(max_length=1, min_length=1)]] = 'N'
    Ce_Under_Bond: Optional[Annotated[str, Field(max_length=1, min_length=1)]] = None
    Ce_Link: Optional[Annotated[str, Field(max_length=1, min_length=1)]] = None
    Product_Price: Optional[Annotated[float, Field(le=999999999999)]] = None
    Product_Currency: Optional[Annotated[str, Field(max_length=3)]] = None
    Ce_Invoice_Number: Optional[Annotated[str, Field(max_length=20)]] = None
    Nls_Calendar: Optional[Annotated[str, Field(max_length=30)]] = None
    Serial_Valid_Merge: Optional[Annotated[str, Field(max_length=1, min_length=1)]] = None
    Sampling_Type: Optional[Annotated[str, Field(max_length=20)]] = None
    Collective_Sequence: Optional[Annotated[int, Field(le=9999999999)]] = None
    Expected_Net_Weight: Optional[Annotated[float, Field(le=9999999999999)]] = None
    Expected_Gross_Weight: Optional[Annotated[float, Field(le=9999999999999)]] = None

    model_config = {
        "str_strip_whitespace": True,
        "extra": "forbid"
    }

    # Validators for Allowed Values
    @field_validator("Record_Type")
    @classmethod
    def record_type_must_be_pal(cls, v: str) -> str:
        if v != "PAL":
            raise ValueError("Record_Type must be 'PAL'")
        return v

    @field_validator("Merge_Action")
    @classmethod
    def merge_action_allowed_values(cls, v: str) -> str:
        if v not in ["A", "U", "D"]:
            raise ValueError("Merge_Action must be 'A', 'U', or 'D'")
        return v

    @field_validator("Disallow_Merge_Rules", "User_Def_Chk_1", "User_Def_Chk_2", "User_Def_Chk_3", 
                     "User_Def_Chk_4", "Collective_Mode", "Ce_Under_Bond", "Ce_Link", "Serial_Valid_Merge")
    @classmethod
    def y_n_flags(cls, v: Optional[str], info) -> Optional[str]:
        if v is not None and v not in ["Y", "N"]:
            raise ValueError(f"{info.field_name} must be 'Y' or 'N'")
        return v

    # Uppercase Validation
    @field_validator("Pre_Advice_Id", "Sku_Id", "Config_Id", "Batch_Id", "Pallet_Config", 
                     "Condition_Id", "Lock_Code", "Tag_Id", "Origin_Id", "Client_Id", 
                     "User_Def_Type_1", "User_Def_Type_2", "User_Def_Type_3", "User_Def_Type_4", 
                     "User_Def_Type_5", "User_Def_Type_6", "User_Def_Type_7", "User_Def_Type_8", 
                     "Spec_Code", "Client_Group", "Tracking_Level", "Host_Pre_Advice_Id", 
                     "Host_Line_Id", "Ce_Coo", "Owner_Id", "Ce_Consignment_Id", "Ce_Invoice_Number", 
                     "Sampling_Type")
    @classmethod
    def enforce_uppercase(cls, v: Optional[str], info) -> Optional[str]:
        if v is not None and v != '' and not v.isupper():
            v = v.upper()
        return v

    # Date Format Validation
    @field_validator("Expiry_Dstamp", "Manuf_Dstamp", "User_Def_Date_1", "User_Def_Date_2", 
                     "User_Def_Date_3", "User_Def_Date_4")
    @classmethod
    def validate_date_format(cls, v: Optional[str], info) -> Optional[str]:
        if v is not None:
            try:
                datetime.strptime(v, "%Y%m%d%H%M%S")
            except ValueError:
                raise ValueError(f"{info.field_name} must be in 'YYYYMMDDHH24MISS' format (e.g., '20230305143000')")
        return v

    # Numeric Range Validation
    @field_validator("Line_Id")
    @classmethod
    def validate_line_id(cls, v: Optional[int], info) -> Optional[int]:
        if v is not None and (v < 0 or v > 999999):
            raise ValueError(f"{info.field_name} must be between 0 and 999999")
        return v

    @field_validator("Collective_Sequence")
    @classmethod
    def validate_collective_sequence(cls, v: Optional[int], info) -> Optional[int]:
        if v is not None and (v < 0 or v > 9999999999):
            raise ValueError(f"{info.field_name} must be between 0 and 9999999999")
        return v

    @field_validator("Qty_Due", "User_Def_Num_1", "User_Def_Num_2", "User_Def_Num_3", "User_Def_Num_4")
    @classmethod
    def validate_decimal_15(cls, v: Optional[float], info) -> Optional[float]:
        if v is not None and (v < -999999999999999 or v > 999999999999999):
            raise ValueError(f"{info.field_name} must be between -999999999999999 and 999999999999999")
        return v

    @field_validator("Qty_Due_Tolerance")
    @classmethod
    def validate_qty_due_tolerance(cls, v: Optional[float], info) -> Optional[float]:
        if v is not None and (v < -999999 or v > 999999):
            raise ValueError(f"{info.field_name} must be between -999999 and 999999")
        return v

    @field_validator("Product_Price")
    @classmethod
    def validate_decimal_12(cls, v: Optional[float], info) -> Optional[float]:
        if v is not None and (v < -999999999999 or v > 999999999999):
            raise ValueError(f"{info.field_name} must be between -999999999999 and 999999999999")
        return v

    @field_validator("Expected_Net_Weight", "Expected_Gross_Weight")
    @classmethod
    def validate_decimal_13(cls, v: Optional[float], info) -> Optional[float]:
        if v is not None and (v < -9999999999999 or v > 9999999999999):
            raise ValueError(f"{info.field_name} must be between -9999999999999 and 9999999999999")
        return v
    
    @field_validator("Collective_Mode", mode="before")
    @classmethod
    def set_default(cls, v):
        return 'N' if v is None else v

# Example Usage
if __name__ == "__main__":
    valid_data = {
        "Record_Type": "PAL",
        "Merge_Action": "A",
        "Pre_Advice_Id": "PA123",
        "Sku_Id": "SKU456",
        "Qty_Due": 123.456,
        "Client_Id": "CLI789",
        "Line_Id": 123,
        "Expiry_Dstamp": "20230305143000",
        "User_Def_Num_1": 12345.6789
    }

    try:
        pre_advice_line = PAL(**valid_data)
        print("Valid data:", pre_advice_line.model_dump())
    except ValueError as e:
        print("Validation error:", str(e))