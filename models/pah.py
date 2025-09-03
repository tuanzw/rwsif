from pydantic import BaseModel, Field, field_validator
from typing import Annotated, Optional
from datetime import datetime

class PAH(BaseModel):
    Record_Type: Annotated[str, Field(max_length=3, min_length=3)]
    Merge_Action: Annotated[str, Field(max_length=1, min_length=1)]
    Pre_Advice_Id: Annotated[str, Field(max_length=20)]
    Site_Id: Optional[Annotated[str, Field(max_length=10)]] = None
    Supplier_Id: Optional[Annotated[str, Field(max_length=15)]] = None
    Status: Optional[Annotated[str, Field(max_length=11)]] = None
    Bookref_Id: Optional[Annotated[str, Field(max_length=20)]] = None
    Due_Dstamp: Optional[Annotated[str, Field(max_length=14, min_length=14)]] = None
    Notes: Optional[Annotated[str, Field(max_length=80)]] = None
    Owner_Id: Optional[Annotated[str, Field(max_length=10)]] = None
    Contact: Optional[Annotated[str, Field(max_length=25)]] = None
    Contact_Phone: Optional[Annotated[str, Field(max_length=25)]] = None
    Contact_Fax: Optional[Annotated[str, Field(max_length=25)]] = None
    Contact_Email: Optional[Annotated[str, Field(max_length=256)]] = None
    Name: Optional[Annotated[str, Field(max_length=50)]] = None
    Address1: Optional[Annotated[str, Field(max_length=60)]] = None
    Address2: Optional[Annotated[str, Field(max_length=60)]] = None
    Town: Optional[Annotated[str, Field(max_length=60)]] = None
    County: Optional[Annotated[str, Field(max_length=60)]] = None
    Postcode: Optional[Annotated[str, Field(max_length=20)]] = None
    Country: Optional[Annotated[str, Field(max_length=25)]] = None
    Pre_Advice_Type: Optional[Annotated[str, Field(max_length=10)]] = None
    Sampling_Type: Optional[Annotated[str, Field(max_length=20)]] = None
    Return_Flag: Optional[Annotated[str, Field(max_length=1, min_length=1)]] = None
    Returned_Order_Id: Optional[Annotated[str, Field(max_length=20)]] = None
    Collection_Reqd: Optional[Annotated[str, Field(max_length=1, min_length=1)]] = None
    Consignment: Optional[Annotated[str, Field(max_length=20)]] = None
    Load_Sequence: Optional[Annotated[int, Field(le=9999999999)]] = None
    Email_Confirm: Optional[Annotated[str, Field(max_length=1, min_length=1)]] = None
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
    Disallow_Replens: Optional[Annotated[str, Field(max_length=1, min_length=1)]] = None
    Client_Group: Optional[Annotated[str, Field(max_length=10)]] = None
    Supplier_Reference: Optional[Annotated[str, Field(max_length=20)]] = None
    Carrier_Name: Optional[Annotated[str, Field(max_length=50)]] = None
    Carrier_Reference: Optional[Annotated[str, Field(max_length=20)]] = None
    Tod: Optional[Annotated[str, Field(max_length=3)]] = None
    Tod_Place: Optional[Annotated[str, Field(max_length=60)]] = None
    Mode_Of_Transport: Optional[Annotated[str, Field(max_length=10)]] = None
    Vat_Number: Optional[Annotated[str, Field(max_length=20)]] = None
    Yard_Container_Type: Optional[Annotated[str, Field(max_length=18)]] = None
    Yard_Container_Id: Optional[Annotated[str, Field(max_length=20)]] = None
    Ce_Consignment_Id: Optional[Annotated[str, Field(max_length=18)]] = None
    Collective_Mode: Optional[Annotated[str, Field(max_length=1, min_length=1)]] = 'N'
    Contact_Mobile: Optional[Annotated[str, Field(max_length=25)]] = None
    Master_Pre_Advice: Optional[Annotated[str, Field(max_length=1, min_length=1)]] = None
    Ce_Invoice_Number: Optional[Annotated[str, Field(max_length=20)]] = None
    Nls_Calendar: Optional[Annotated[str, Field(max_length=30)]] = None
    Status_Reason_Code: Optional[Annotated[str, Field(max_length=10)]] = None
    Priority: Optional[Annotated[int, Field(le=9999)]] = None
    Collective_Sequence: Optional[Annotated[int, Field(le=9999999999)]] = None

    model_config = {
        "str_strip_whitespace": True,
        "extra": "forbid"
    }

    # Validators for Allowed Values
    @field_validator("Record_Type")
    @classmethod
    def record_type_must_be_pah(cls, v: str) -> str:
        if v != "PAH":
            raise ValueError("Record_Type must be 'PAH'")
        return v

    @field_validator("Merge_Action")
    @classmethod
    def merge_action_allowed_values(cls, v: str) -> str:
        if v not in ["A", "U", "D"]:
            raise ValueError("Merge_Action must be 'A', 'U', or 'D'")
        return v

    @field_validator("Status")
    @classmethod
    def status_allowed_values(cls, v: Optional[str]) -> Optional[str]:
        if v is not None and v not in ["Complete", "Hold", "In Progress", "Released"]:
            raise ValueError("Status must be one of: 'Complete', 'Hold', 'In Progress', 'Released'")
        return v

    @field_validator("Return_Flag", "Collection_Reqd", "Email_Confirm", "Disallow_Merge_Rules", 
                     "User_Def_Chk_1", "User_Def_Chk_2", "User_Def_Chk_3", "User_Def_Chk_4", 
                     "Disallow_Replens", "Collective_Mode", "Master_Pre_Advice")
    @classmethod
    def y_n_flags(cls, v: Optional[str], info) -> Optional[str]:
        if v is not None and v not in ["Y", "N"]:
            raise ValueError(f"{info.field_name} must be 'Y' or 'N'")
        return v

    # Uppercase Validation
    @field_validator("Pre_Advice_Id", "Site_Id", "Supplier_Id", "Bookref_Id", "Owner_Id", 
                     "Postcode", "Country", "Pre_Advice_Type", "Sampling_Type", "Returned_Order_Id", 
                     "Consignment", "Client_Id", "User_Def_Type_1", "User_Def_Type_2", 
                     "User_Def_Type_3", "User_Def_Type_4", "User_Def_Type_5", "User_Def_Type_6", 
                     "User_Def_Type_7", "User_Def_Type_8", "Client_Group", "Supplier_Reference", 
                     "Tod", "Mode_Of_Transport", "Yard_Container_Type", "Yard_Container_Id", 
                     "Ce_Consignment_Id", "Ce_Invoice_Number", "Status_Reason_Code")
    @classmethod
    def enforce_uppercase(cls, v: Optional[str], info) -> Optional[str]:
        if v is not None and v != '' and not v.isupper():
            v = v.upper()
        return v

    # Date Format Validation
    @field_validator("Due_Dstamp", "User_Def_Date_1", "User_Def_Date_2", "User_Def_Date_3", 
                     "User_Def_Date_4")
    @classmethod
    def validate_date_format(cls, v: Optional[str], info) -> Optional[str]:
        if v is not None:
            try:
                datetime.strptime(v, "%Y%m%d%H%M%S")
            except ValueError:
                raise ValueError(f"{info.field_name} must be in 'YYYYMMDDHH24MISS' format (e.g., '20230305143000')")
        return v

    # Numeric Range Validation
    @field_validator("Load_Sequence", "Collective_Sequence")
    @classmethod
    def validate_int_range(cls, v: Optional[int], info) -> Optional[int]:
        if v is not None and (v < 0 or v > 9999999999):
            raise ValueError(f"{info.field_name} must be between 0 and 9999999999")
        return v

    @field_validator("Priority")
    @classmethod
    def validate_priority(cls, v: Optional[int], info) -> Optional[int]:
        if v is not None and (v < 0 or v > 9999):
            raise ValueError(f"{info.field_name} must be between 0 and 9999")
        return v

    @field_validator("User_Def_Num_1", "User_Def_Num_2", "User_Def_Num_3", "User_Def_Num_4")
    @classmethod
    def validate_decimal_15(cls, v: Optional[float], info) -> Optional[float]:
        if v is not None and (v < -999999999999999 or v > 999999999999999):
            raise ValueError(f"{info.field_name} must be between -999999999999999 and 999999999999999")
        return v
    
    @field_validator("Collective_Mode", mode="before")
    @classmethod
    def set_default(cls, v):
        return 'N' if v is None else v

# Example Usage
if __name__ == "__main__":
    valid_data = {
        "Record_Type": "PAH",
        "Merge_Action": "A",
        "Pre_Advice_Id": "PA123",
        "Client_Id": "CLI456",
        "Status": "In Progress",
        "Due_Dstamp": "20230305143000",
        "Return_Flag": "Y",
        "User_Def_Num_1": 12345.6789
    }

    try:
        pre_advice = PAH(**valid_data)
        print("Valid data:", pre_advice.model_dump())
    except ValueError as e:
        print("Validation error:", str(e))