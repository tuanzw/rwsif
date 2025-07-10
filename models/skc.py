from pydantic import BaseModel, Field, field_validator
from typing import Annotated, Optional
from datetime import datetime

class SKC(BaseModel):
    Record_Type: Annotated[str, Field(max_length=3, min_length=3)]
    Merge_Action: Annotated[str, Field(max_length=1, min_length=1)]
    Config_Id: Annotated[str, Field(max_length=15)]
    Client_Id: Annotated[str, Field(max_length=10)]
    Tag_Volume: Annotated[float, Field(ge=0, le=9999999.999999)]
    Track_Level_1: Annotated[str, Field(max_length=8)]
    Ratio_1_To_2: Optional[Annotated[float, Field(ge=0, le=999999.999999)]] = None
    Track_Level_2: Optional[Annotated[str, Field(max_length=8)]] = None
    Ratio_2_To_3: Optional[Annotated[int, Field(ge=0, le=999999)]] = None
    Track_Level_3: Optional[Annotated[str, Field(max_length=8)]] = None
    Ratio_3_To_4: Optional[Annotated[int, Field(ge=0, le=999999)]] = None
    Track_Level_4: Optional[Annotated[str, Field(max_length=8)]] = None
    Ratio_4_To_5: Optional[Annotated[int, Field(ge=0, le=999999)]] = None
    Track_Level_5: Optional[Annotated[str, Field(max_length=8)]] = None
    Ratio_5_To_6: Optional[Annotated[int, Field(ge=0, le=999999)]] = None
    Track_Level_6: Optional[Annotated[str, Field(max_length=8)]] = None
    Ratio_6_To_7: Optional[Annotated[int, Field(ge=0, le=999999)]] = None
    Track_Level_7: Optional[Annotated[str, Field(max_length=8)]] = None
    Ratio_7_To_8: Optional[Annotated[int, Field(ge=0, le=999999)]] = None
    Track_Level_8: Optional[Annotated[str, Field(max_length=8)]] = None
    Notes: Optional[Annotated[str, Field(max_length=80)]] = None
    Split_Lowest: Optional[Annotated[str, Field(max_length=1)]] = None
    Each_Per_Layer: Optional[Annotated[int, Field(ge=0, le=999999)]] = None
    Layer_Height: Optional[Annotated[float, Field(ge=0, le=999999999.999999)]] = None
    Volume_At_Each: Optional[Annotated[str, Field(max_length=1)]] = None
    Volume_2: Optional[Annotated[float, Field(ge=0, le=9999999.999999)]] = None
    Weight_2: Optional[Annotated[float, Field(ge=0, le=9999999.999999)]] = None
    Height_2: Optional[Annotated[float, Field(ge=0, le=999999999.999999)]] = None
    Width_2: Optional[Annotated[float, Field(ge=0, le=9999.999)]] = None
    Depth_2: Optional[Annotated[float, Field(ge=0, le=9999.999)]] = None
    Volume_3: Optional[Annotated[float, Field(ge=0, le=9999999.999999)]] = None
    Weight_3: Optional[Annotated[float, Field(ge=0, le=9999999.999999)]] = None
    Height_3: Optional[Annotated[float, Field(ge=0, le=999999999.999999)]] = None
    Width_3: Optional[Annotated[float, Field(ge=0, le=9999.999)]] = None
    Depth_3: Optional[Annotated[float, Field(ge=0, le=9999.999)]] = None
    Volume_4: Optional[Annotated[float, Field(ge=0, le=9999999.999999)]] = None
    Weight_4: Optional[Annotated[float, Field(ge=0, le=9999999.999999)]] = None
    Height_4: Optional[Annotated[float, Field(ge=0, le=999999999.999999)]] = None
    Width_4: Optional[Annotated[float, Field(ge=0, le=9999.999)]] = None
    Depth_4: Optional[Annotated[float, Field(ge=0, le=9999.999)]] = None
    Volume_5: Optional[Annotated[float, Field(ge=0, le=9999999.999999)]] = None
    Weight_5: Optional[Annotated[float, Field(ge=0, le=9999999.999999)]] = None
    Height_5: Optional[Annotated[float, Field(ge=0, le=999999999.999999)]] = None
    Width_5: Optional[Annotated[float, Field(ge=0, le=9999.999)]] = None
    Depth_5: Optional[Annotated[float, Field(ge=0, le=9999.999)]] = None
    Volume_6: Optional[Annotated[float, Field(ge=0, le=9999999.999999)]] = None
    Weight_6: Optional[Annotated[float, Field(ge=0, le=9999999.999999)]] = None
    Height_6: Optional[Annotated[float, Field(ge=0, le=999999999.999999)]] = None
    Width_6: Optional[Annotated[float, Field(ge=0, le=9999.999)]] = None
    Depth_6: Optional[Annotated[float, Field(ge=0, le=9999.999)]] = None
    Volume_7: Optional[Annotated[float, Field(ge=0, le=9999999.999999)]] = None
    Weight_7: Optional[Annotated[float, Field(ge=0, le=9999999.999999)]] = None
    Height_7: Optional[Annotated[float, Field(ge=0, le=999999999.999999)]] = None
    Width_7: Optional[Annotated[float, Field(ge=0, le=9999.999)]] = None
    Depth_7: Optional[Annotated[float, Field(ge=0, le=9999.999)]] = None
    Time_Zone_Name: Optional[Annotated[str, Field(max_length=64)]] = None
    Performance_Factor: Optional[Annotated[float, Field(ge=0, le=999999.999999)]] = None
    Volume_8: Optional[Annotated[float, Field(ge=0, le=9999999.999999)]] = None
    Weight_8: Optional[Annotated[float, Field(ge=0, le=9999999.999999)]] = None
    Height_8: Optional[Annotated[float, Field(ge=0, le=999999999.999999)]] = None
    Width_8: Optional[Annotated[float, Field(ge=0, le=9999.999)]] = None
    Depth_8: Optional[Annotated[float, Field(ge=0, le=9999.999)]] = None
    Stage_Route_Id_1: Optional[Annotated[str, Field(max_length=20)]] = None
    Stage_Route_Id_2: Optional[Annotated[str, Field(max_length=20)]] = None
    Stage_Route_Id_3: Optional[Annotated[str, Field(max_length=20)]] = None
    Stage_Route_Id_4: Optional[Annotated[str, Field(max_length=20)]] = None
    Stage_Route_Id_5: Optional[Annotated[str, Field(max_length=20)]] = None
    Stage_Route_Id_6: Optional[Annotated[str, Field(max_length=20)]] = None
    Stage_Route_Id_7: Optional[Annotated[str, Field(max_length=20)]] = None
    Stage_Route_Id_8: Optional[Annotated[str, Field(max_length=20)]] = None
    Labor_C1_Track_Level: Optional[Annotated[int, Field(ge=0, le=9)]] = None
    Labor_C2_Track_Level: Optional[Annotated[int, Field(ge=0, le=9)]] = None
    Labor_H1_Track_Level: Optional[Annotated[int, Field(ge=0, le=9)]] = None
    Labor_H2_Track_Level: Optional[Annotated[int, Field(ge=0, le=9)]] = None
    Labor_H3_Track_Level: Optional[Annotated[int, Field(ge=0, le=9)]] = None
    Shipping_Unit_Lev_1: Optional[Annotated[str, Field(max_length=1)]] = None
    Shipping_Unit_Lev_2: Optional[Annotated[str, Field(max_length=1)]] = None
    Shipping_Unit_Lev_3: Optional[Annotated[str, Field(max_length=1)]] = None
    Shipping_Unit_Lev_4: Optional[Annotated[str, Field(max_length=1)]] = None
    Shipping_Unit_Lev_5: Optional[Annotated[str, Field(max_length=1)]] = None
    Shipping_Unit_Lev_6: Optional[Annotated[str, Field(max_length=1)]] = None
    Shipping_Unit_Lev_7: Optional[Annotated[str, Field(max_length=1)]] = None
    Shipping_Unit_Lev_8: Optional[Annotated[str, Field(max_length=1)]] = None
    Nls_Calendar: Optional[Annotated[str, Field(max_length=30)]] = None
    Rdt_Display_Lev_1: Optional[Annotated[str, Field(max_length=1)]] = None
    Rdt_Display_Lev_2: Optional[Annotated[str, Field(max_length=1)]] = None
    Rdt_Display_Lev_3: Optional[Annotated[str, Field(max_length=1)]] = None
    Rdt_Display_Lev_4: Optional[Annotated[str, Field(max_length=1)]] = None
    Rdt_Display_Lev_5: Optional[Annotated[str, Field(max_length=1)]] = None
    Rdt_Display_Lev_6: Optional[Annotated[str, Field(max_length=1)]] = None
    Rdt_Display_Lev_7: Optional[Annotated[str, Field(max_length=1)]] = None
    Rdt_Display_Lev_8: Optional[Annotated[str, Field(max_length=1)]] = None
    Disallow_Merge_Rules: Optional[Annotated[str, Field(max_length=1)]] = None
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
    User_Def_Num_1: Optional[Annotated[float, Field(ge=0, le=999999999.999999)]] = None
    User_Def_Num_2: Optional[Annotated[float, Field(ge=0, le=999999999.999999)]] = None
    User_Def_Num_3: Optional[Annotated[float, Field(ge=0, le=999999999.999999)]] = None
    User_Def_Num_4: Optional[Annotated[float, Field(ge=0, le=999999999.999999)]] = None
    User_Def_Note_1: Optional[Annotated[str, Field(max_length=200)]] = None
    User_Def_Note_2: Optional[Annotated[str, Field(max_length=200)]] = None
    Client_Group: Optional[Annotated[str, Field(max_length=10)]] = None
    Rdt_Track_Level_1: Optional[Annotated[str, Field(max_length=8)]] = None
    Rdt_Track_Level_2: Optional[Annotated[str, Field(max_length=8)]] = None
    Rdt_Track_Level_3: Optional[Annotated[str, Field(max_length=8)]] = None
    Rdt_Track_Level_4: Optional[Annotated[str, Field(max_length=8)]] = None
    Rdt_Track_Level_5: Optional[Annotated[str, Field(max_length=8)]] = None
    Rdt_Track_Level_6: Optional[Annotated[str, Field(max_length=8)]] = None
    Rdt_Track_Level_7: Optional[Annotated[str, Field(max_length=8)]] = None
    Rdt_Track_Level_8: Optional[Annotated[str, Field(max_length=8)]] = None

    model_config = {
        "str_strip_whitespace": True,
        "extra": "forbid"
    }

    # Validators for Allowed Values
    @field_validator("Record_Type")
    @classmethod
    def record_type_must_be_skc(cls, v: str) -> str:
        if v != "SKC":
            raise ValueError("Record_Type must be 'SKC'")
        return v

    @field_validator("Merge_Action")
    @classmethod
    def merge_action_allowed_values(cls, v: str) -> str:
        if v not in ["A", "U", "D"]:
            raise ValueError("Merge_Action must be 'A', 'U', or 'D'")
        return v

    @field_validator("Split_Lowest", "Volume_At_Each", "Shipping_Unit_Lev_1", 
                    "Shipping_Unit_Lev_2", "Shipping_Unit_Lev_3", "Shipping_Unit_Lev_4",
                    "Shipping_Unit_Lev_5", "Shipping_Unit_Lev_6", "Shipping_Unit_Lev_7",
                    "Shipping_Unit_Lev_8", "Rdt_Display_Lev_1", "Rdt_Display_Lev_2",
                    "Rdt_Display_Lev_3", "Rdt_Display_Lev_4", "Rdt_Display_Lev_5",
                    "Rdt_Display_Lev_6", "Rdt_Display_Lev_7", "Rdt_Display_Lev_8",
                    "Disallow_Merge_Rules", "User_Def_Chk_1", "User_Def_Chk_2",
                    "User_Def_Chk_3", "User_Def_Chk_4")
    @classmethod
    def y_n_flags(cls, v: Optional[str], info) -> Optional[str]:
        if v is not None and v not in ["Y", "N"]:
            raise ValueError(f"{info.field_name} must be 'Y' or 'N'")
        return v

    # Uppercase Validation
    @field_validator("Config_Id", "Client_Id", "Track_Level_1", "Track_Level_2",
                    "Track_Level_3", "Track_Level_4", "Track_Level_5", "Track_Level_6",
                    "Track_Level_7", "Track_Level_8", "Stage_Route_Id_1", "Stage_Route_Id_2",
                    "Stage_Route_Id_3", "Stage_Route_Id_4", "Stage_Route_Id_5", "Stage_Route_Id_6",
                    "Stage_Route_Id_7", "Stage_Route_Id_8", "User_Def_Type_1", "User_Def_Type_2",
                    "User_Def_Type_3", "User_Def_Type_4", "User_Def_Type_5", "User_Def_Type_6",
                    "User_Def_Type_7", "User_Def_Type_8", "Client_Group", "Rdt_Track_Level_1",
                    "Rdt_Track_Level_2", "Rdt_Track_Level_3", "Rdt_Track_Level_4", "Rdt_Track_Level_5",
                    "Rdt_Track_Level_6", "Rdt_Track_Level_7", "Rdt_Track_Level_8")
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

# Example Usage
if __name__ == "__main__":
    valid_data = {
        "Record_Type": "SKC",
        "Merge_Action": "A",
        "Config_Id": "CONFIG123",
        "Client_Id": "CLIENT1",
        "Tag_Volume": 100.5,
        "Track_Level_1": "PALLET",
        "Ratio_1_To_2": 4.0,
        "Split_Lowest": "Y",
        "User_Def_Date_1": "20230305143000"
    }

    try:
        skc = SKC(**valid_data)
        print("Valid data:", skc.model_dump())
    except ValueError as e:
        print("Validation error:", str(e))