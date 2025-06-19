from pydantic import BaseModel, Field, field_validator
from typing import Annotated, Optional
from datetime import datetime

class ODL(BaseModel):
    Record_Type: Annotated[str, Field(max_length=3, min_length=3)]
    Merge_Action: Annotated[str, Field(max_length=1, min_length=1)]
    Order_Id: Annotated[str, Field(max_length=20)]
    Line_Id: Annotated[int, Field(le=999999)]
    Sku_Id: Annotated[str, Field(max_length=50)]
    Config_Id: Optional[Annotated[str, Field(max_length=15)]] = None
    Tracking_Level: Optional[Annotated[str, Field(max_length=8)]] = None
    Batch_Id: Optional[Annotated[str, Field(max_length=20)]] = None
    Batch_Mixing: Optional[Annotated[str, Field(max_length=1, min_length=1)]] = None
    Condition_Id: Optional[Annotated[str, Field(max_length=10)]] = None
    Lock_Code: Optional[Annotated[str, Field(max_length=10)]] = None
    Qty_Ordered: Annotated[float, Field(le=999999999999999)]
    Allocate: Optional[Annotated[str, Field(max_length=1, min_length=1)]] = None
    Back_Ordered: Optional[Annotated[str, Field(max_length=1, min_length=1)]] = None
    Deallocate: Optional[Annotated[str, Field(max_length=1, min_length=1)]] = None
    Kit_Split: Optional[Annotated[str, Field(max_length=1, min_length=1)]] = None
    Origin_Id: Optional[Annotated[str, Field(max_length=10)]] = None
    Notes: Optional[Annotated[str, Field(max_length=80)]] = None
    Customer_Sku_Id: Optional[Annotated[str, Field(max_length=50)]] = None
    Shelf_Life_Days: Optional[Annotated[int, Field(le=99999)]] = None
    Shelf_Life_Percent: Optional[Annotated[int, Field(le=999)]] = None
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
    Soh_Id: Optional[Annotated[str, Field(max_length=4)]] = None
    Line_Value: Optional[Annotated[float, Field(le=999999999999)]] = None
    Time_Zone_Name: Optional[Annotated[str, Field(max_length=64)]] = None
    Spec_Code: Optional[Annotated[str, Field(max_length=99)]] = None
    Rule_Id: Optional[Annotated[str, Field(max_length=10)]] = None
    Client_Group: Optional[Annotated[str, Field(max_length=10)]] = None
    Task_Per_Each: Optional[Annotated[str, Field(max_length=1, min_length=1)]] = None
    Use_Pick_To_Grid: Optional[Annotated[str, Field(max_length=1, min_length=1)]] = None
    Ignore_Weight_Capture: Optional[Annotated[str, Field(max_length=1, min_length=1)]] = None
    Host_Order_Id: Optional[Annotated[str, Field(max_length=20)]] = None
    Host_Line_Id: Optional[Annotated[str, Field(max_length=20)]] = None
    Stage_Route_Id: Optional[Annotated[str, Field(max_length=20)]] = None
    Min_Qty_Ordered: Optional[Annotated[float, Field(le=999999999999999)]] = None
    Max_Qty_Ordered: Optional[Annotated[float, Field(le=999999999999999)]] = None
    Expected_Value: Optional[Annotated[float, Field(le=999999999999)]] = None
    Expected_Volume: Optional[Annotated[float, Field(le=999999999999999)]] = None
    Expected_Weight: Optional[Annotated[float, Field(le=999999999999999)]] = None
    Customer_Sku_Desc1: Optional[Annotated[str, Field(max_length=80)]] = None
    Customer_Sku_Desc2: Optional[Annotated[str, Field(max_length=80)]] = None
    Purchase_Order: Optional[Annotated[str, Field(max_length=25)]] = None
    Product_Price: Optional[Annotated[float, Field(le=999999999999)]] = None
    Product_Currency: Optional[Annotated[str, Field(max_length=3)]] = None
    Documentation_Unit: Optional[Annotated[str, Field(max_length=8)]] = None
    Extended_Price: Optional[Annotated[float, Field(le=999999999999)]] = None
    Tax_1: Optional[Annotated[float, Field(le=999999999999)]] = None
    Tax_2: Optional[Annotated[float, Field(le=999999999999)]] = None
    Documentation_Text_1: Optional[Annotated[str, Field(max_length=180)]] = None
    Serial_Number: Optional[Annotated[str, Field(max_length=30)]] = None
    Owner_Id: Optional[Annotated[str, Field(max_length=10)]] = None
    Collective_Mode: Optional[Annotated[str, Field(max_length=1, min_length=1)]] = None
    Ce_Receipt_Type: Optional[Annotated[str, Field(max_length=2)]] = None
    Ce_Coo: Optional[Annotated[str, Field(max_length=3)]] = None
    Kit_Plan_Id: Optional[Annotated[str, Field(max_length=30)]] = None
    Location_Id: Optional[Annotated[str, Field(max_length=20)]] = None
    Nls_Calendar: Optional[Annotated[str, Field(max_length=30)]] = None
    Collective_Sequence: Optional[Annotated[int, Field(le=9999999999)]] = None
    Unallocatable: Optional[Annotated[str, Field(max_length=1, min_length=1)]] = None
    Full_Tracking_Level_Only: Optional[Annotated[str, Field(max_length=1, min_length=1)]] = None
    Min_Full_Pallet_Perc: Optional[Annotated[int, Field(le=999)]] = None
    Max_Full_Pallet_Perc: Optional[Annotated[int, Field(le=999)]] = None
    Substitute_Grade: Optional[Annotated[str, Field(max_length=10)]] = None
    Disallow_Substitution: Optional[Annotated[str, Field(max_length=1, min_length=1)]] = None
    Final_Order_Line: Optional[Annotated[str, Field(max_length=1, min_length=1)]] = None

    model_config = {
        "str_strip_whitespace": True,
        "extra": "forbid"
    }

    # Validators for Allowed Values
    @field_validator("Record_Type")
    @classmethod
    def record_type_must_be_odl(cls, v: str) -> str:
        if v != "ODL":
            raise ValueError("Record_Type must be 'ODL'")
        return v

    @field_validator("Merge_Action")
    @classmethod
    def merge_action_allowed_values(cls, v: str) -> str:
        if v not in ["A", "U", "D"]:
            raise ValueError("Merge_Action must be 'A', 'U', or 'D'")
        return v

    @field_validator("Batch_Mixing", "Allocate", "Back_Ordered", "Deallocate", "Kit_Split", 
                     "Disallow_Merge_Rules", "User_Def_Chk_1", "User_Def_Chk_2", "User_Def_Chk_3", 
                     "User_Def_Chk_4", "Task_Per_Each", "Use_Pick_To_Grid", "Ignore_Weight_Capture", 
                     "Collective_Mode", "Unallocatable", "Full_Tracking_Level_Only", 
                     "Disallow_Substitution", "Final_Order_Line")
    @classmethod
    def y_n_flags(cls, v: Optional[str], info) -> Optional[str]:
        if v is not None and v not in ["Y", "N"]:
            raise ValueError(f"{info.field_name} must be 'Y' or 'N'")
        return v

    # Uppercase Validation
    @field_validator("Order_Id", "Sku_Id", "Config_Id", "Tracking_Level", "Batch_Id", 
                     "Condition_Id", "Lock_Code", "Origin_Id", "Customer_Sku_Id", "Client_Id", 
                     "User_Def_Type_1", "User_Def_Type_2", "User_Def_Type_3", "User_Def_Type_4", 
                     "User_Def_Type_5", "User_Def_Type_6", "User_Def_Type_7", "User_Def_Type_8", 
                     "Soh_Id", "Spec_Code", "Rule_Id", "Client_Group", "Host_Order_Id", 
                     "Host_Line_Id", "Stage_Route_Id", "Purchase_Order", "Owner_Id", 
                     "Ce_Receipt_Type", "Ce_Coo", "Kit_Plan_Id", "Location_Id", "Substitute_Grade")
    @classmethod
    def enforce_uppercase(cls, v: Optional[str], info) -> Optional[str]:
        if v is not None and v != '' and not v.isupper():
            v = v.upper()
        return v

    # Date Format Validation
    @field_validator("User_Def_Date_1", "User_Def_Date_2", "User_Def_Date_3", "User_Def_Date_4")
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

    @field_validator("Shelf_Life_Days")
    @classmethod
    def validate_shelf_life_days(cls, v: Optional[int], info) -> Optional[int]:
        if v is not None and (v < 0 or v > 99999):
            raise ValueError(f"{info.field_name} must be between 0 and 99999")
        return v

    @field_validator("Shelf_Life_Percent", "Min_Full_Pallet_Perc", "Max_Full_Pallet_Perc")
    @classmethod
    def validate_percentage(cls, v: Optional[int], info) -> Optional[int]:
        if v is not None and (v < 0 or v > 999):
            raise ValueError(f"{info.field_name} must be between 0 and 999")
        return v

    @field_validator("Collective_Sequence")
    @classmethod
    def validate_collective_sequence(cls, v: Optional[int], info) -> Optional[int]:
        if v is not None and (v < 0 or v > 9999999999):
            raise ValueError(f"{info.field_name} must be between 0 and 9999999999")
        return v

    @field_validator("Qty_Ordered", "User_Def_Num_1", "User_Def_Num_2", "User_Def_Num_3", 
                     "User_Def_Num_4", "Min_Qty_Ordered", "Max_Qty_Ordered", "Expected_Volume", 
                     "Expected_Weight")
    @classmethod
    def validate_decimal_15(cls, v: Optional[float], info) -> Optional[float]:
        if v is not None and (v < -999999999999999 or v > 999999999999999):
            raise ValueError(f"{info.field_name} must be between -999999999999999 and 999999999999999")
        return v

    @field_validator("Line_Value", "Expected_Value", "Product_Price", "Extended_Price", 
                     "Tax_1", "Tax_2")
    @classmethod
    def validate_decimal_12(cls, v: Optional[float], info) -> Optional[float]:
        if v is not None and (v < -999999999999 or v > 999999999999):
            raise ValueError(f"{info.field_name} must be between -999999999999 and 999999999999")
        return v

# Example Usage
if __name__ == "__main__":
    valid_data = {
        "Record_Type": "ODL",
        "Merge_Action": "A",
        "Order_Id": "ORDER123",
        "Sku_Id": "SKU456",
        "Qty_Ordered": 123.456,
        "Client_Id": "CLI789",
        "Line_Id": 123,
        "Batch_Mixing": "Y",
        "User_Def_Num_1": 12345.6789
    }

    try:
        order_line = ODL(**valid_data)
        print("Valid data:", order_line.model_dump())
    except ValueError as e:
        print("Validation error:", str(e))