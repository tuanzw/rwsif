from pydantic import BaseModel, Field, field_validator
from typing import Annotated, Optional
from datetime import datetime

class SKU(BaseModel):
    Record_Type: Annotated[str, Field(max_length=3, min_length=3)]
    Merge_Action: Annotated[str, Field(max_length=1, min_length=1)]
    Sku_Id: Annotated[str, Field(max_length=50)]
    Ean: Optional[Annotated[str, Field(max_length=14)]] = None
    Description: Annotated[str, Field(max_length=80)]
    Product_Group: Optional[Annotated[str, Field(max_length=10)]] = None
    Allocation_Group: Optional[Annotated[str, Field(max_length=10)]] = None
    Putaway_Group: Optional[Annotated[str, Field(max_length=10)]] = None
    Each_Height: Optional[Annotated[float, Field(ge=0, le=999999999.999999)]] = None
    Each_Weight: Optional[Annotated[float, Field(ge=0, le=9999999.999999)]] = None
    Each_Volume: Optional[Annotated[float, Field(ge=0, le=9999999.999999)]] = None
    Qc_Status: Optional[Annotated[str, Field(max_length=20)]] = None
    Expiry_Reqd: Optional[Annotated[str, Field(max_length=1)]] = None
    Shelf_Life: Optional[Annotated[int, Field(ge=0, le=99999)]] = None
    Qc_Frequency: Optional[Annotated[int, Field(ge=0, le=9999)]] = None
    Split_Lowest: Optional[Annotated[str, Field(max_length=1)]] = None
    Condition_Reqd: Optional[Annotated[str, Field(max_length=1)]] = None
    Origin_Reqd: Optional[Annotated[str, Field(max_length=1)]] = None
    Serial_At_Pick: Optional[Annotated[str, Field(max_length=1)]] = None
    Serial_At_Pack: Optional[Annotated[str, Field(max_length=1)]] = None
    Pick_Count_Qty: Optional[Annotated[float, Field(ge=0, le=999999999.999999)]] = None
    Count_Frequency: Optional[Annotated[int, Field(ge=0, le=999)]] = None
    Kit_Sku: Optional[Annotated[str, Field(max_length=1)]] = None
    Kit_Split: Optional[Annotated[str, Field(max_length=1)]] = None
    Kitting_Loc_Id: Optional[Annotated[str, Field(max_length=20)]] = None
    Abc_Disable: Optional[Annotated[str, Field(max_length=1)]] = None
    Handling_Class: Optional[Annotated[str, Field(max_length=10)]] = None
    Obsolete_Product: Optional[Annotated[str, Field(max_length=1)]] = None
    New_Product: Optional[Annotated[str, Field(max_length=1)]] = None
    Disallow_Upload: Optional[Annotated[str, Field(max_length=1)]] = None
    Manuf_Dstamp_Reqd: Optional[Annotated[str, Field(max_length=1)]] = None
    Manuf_Dstamp_Dflt: Optional[Annotated[str, Field(max_length=1)]] = None
    Min_Shelf_Life: Optional[Annotated[int, Field(ge=0, le=99999)]] = None
    Colour: Optional[Annotated[str, Field(max_length=20)]] = None
    Sku_Size: Optional[Annotated[str, Field(max_length=10)]] = None
    Hazmat: Optional[Annotated[str, Field(max_length=1)]] = None
    Hazmat_Id: Optional[Annotated[str, Field(max_length=10)]] = None
    Disallow_Cross_Dock: Optional[Annotated[str, Field(max_length=1)]] = None
    Upc: Optional[Annotated[str, Field(max_length=14)]] = None
    Ship_Shelf_Life: Optional[Annotated[int, Field(ge=0, le=99999)]] = None
    Nmfc_Number: Optional[Annotated[int, Field(ge=0, le=999999)]] = None
    Each_Value: Optional[Annotated[float, Field(ge=0, le=999999999.999)]] = None
    Client_Id: Annotated[str, Field(max_length=10)]
    Incub_Rule: Optional[Annotated[str, Field(max_length=1)]] = None
    Incub_Hours: Optional[Annotated[int, Field(ge=0, le=9999)]] = None
    Each_Width: Optional[Annotated[float, Field(ge=0, le=9999.999)]] = None
    Each_Depth: Optional[Annotated[float, Field(ge=0, le=9999.999)]] = None
    Reorder_Trigger_Qty: Optional[Annotated[float, Field(ge=0, le=999999999.999999)]] = None
    Low_Trigger_Qty: Optional[Annotated[float, Field(ge=0, le=999999999.999999)]] = None
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
    Disallow_Merge_Rules: Optional[Annotated[str, Field(max_length=1)]] = None
    Pack_Despatch_Repack: Optional[Annotated[str, Field(max_length=1)]] = None
    Serial_At_Receipt: Optional[Annotated[str, Field(max_length=1)]] = None
    Serial_Valid_Merge: Optional[Annotated[str, Field(max_length=1)]] = None
    Serial_No_Reuse: Optional[Annotated[str, Field(max_length=1)]] = None
    Serial_Format: Optional[Annotated[str, Field(max_length=30)]] = None
    Serial_Range: Optional[Annotated[str, Field(max_length=4)]] = None
    Spec_Id: Optional[Annotated[str, Field(max_length=10)]] = None
    Time_Zone_Name: Optional[Annotated[str, Field(max_length=64)]] = None
    Beam_Units: Optional[Annotated[int, Field(ge=0, le=99)]] = None
    Pick_Sequence: Optional[Annotated[int, Field(ge=0, le=999999)]] = None
    Ce_Warehouse_Type: Optional[Annotated[str, Field(max_length=1)]] = None
    Ce_Customs_Excise: Optional[Annotated[str, Field(max_length=1)]] = None
    Ce_Standard_Cost: Optional[Annotated[float, Field(ge=0, le=9999999999999.99)]] = None
    Ce_Standard_Currency: Optional[Annotated[str, Field(max_length=3)]] = None
    Disallow_Clustering: Optional[Annotated[str, Field(max_length=1)]] = None
    Client_Group: Optional[Annotated[str, Field(max_length=10)]] = None
    Max_Stack: Optional[Annotated[int, Field(ge=0, le=99)]] = None
    Stack_Description: Optional[Annotated[str, Field(max_length=30)]] = None
    Stack_Limitation: Optional[Annotated[int, Field(ge=0, le=99)]] = None
    Ce_Duty_Stamp: Optional[Annotated[str, Field(max_length=1)]] = None
    Capture_Weight: Optional[Annotated[str, Field(max_length=1)]] = None
    Weigh_At_Receipt: Optional[Annotated[str, Field(max_length=1)]] = None
    Upper_Weight_Tolerance: Optional[Annotated[float, Field(ge=0, le=999.999)]] = None
    Lower_Weight_Tolerance: Optional[Annotated[float, Field(ge=0, le=999.999)]] = None
    Serial_At_Loading: Optional[Annotated[str, Field(max_length=1)]] = None
    Serial_At_Kitting: Optional[Annotated[str, Field(max_length=1)]] = None
    Serial_At_Unkitting: Optional[Annotated[str, Field(max_length=1)]] = None
    Ce_Commodity_Code: Optional[Annotated[str, Field(max_length=20)]] = None
    Ce_Coo: Optional[Annotated[str, Field(max_length=3)]] = None
    Ce_Cwc: Optional[Annotated[str, Field(max_length=3)]] = None
    Ce_Vat_Code: Optional[Annotated[str, Field(max_length=1)]] = None
    Ce_Product_Type: Optional[Annotated[str, Field(max_length=1)]] = None
    Commodity_Code: Optional[Annotated[str, Field(max_length=22)]] = None
    Commodity_Desc: Optional[Annotated[str, Field(max_length=35)]] = None
    Family_Group: Optional[Annotated[str, Field(max_length=15)]] = None
    Breakpack: Optional[Annotated[str, Field(max_length=1)]] = None
    Clearable: Optional[Annotated[str, Field(max_length=1)]] = None
    Stage_Route_Id: Optional[Annotated[str, Field(max_length=20)]] = None
    Serial_Max_Range: Optional[Annotated[int, Field(ge=0, le=9999)]] = None
    Serial_Dynamic_Range: Optional[Annotated[str, Field(max_length=1)]] = None
    Expiry_At_Repack: Optional[Annotated[str, Field(max_length=1)]] = None
    Udf_At_Repack: Optional[Annotated[str, Field(max_length=1)]] = None
    Manufacture_At_Repack: Optional[Annotated[str, Field(max_length=1)]] = None
    Repack_By_Piece: Optional[Annotated[str, Field(max_length=1)]] = None
    Each_Quantity: Optional[Annotated[float, Field(ge=0, le=999999999.999999)]] = None
    Collective_Mode: Optional[Annotated[str, Field(max_length=1)]] = None
    Packed_Height: Optional[Annotated[float, Field(ge=0, le=9999999.999999)]] = None
    Packed_Width: Optional[Annotated[float, Field(ge=0, le=9999999.999999)]] = None
    Packed_Depth: Optional[Annotated[float, Field(ge=0, le=9999999.999999)]] = None
    Packed_Volume: Optional[Annotated[float, Field(ge=0, le=9999999.999999)]] = None
    Packed_Weight: Optional[Annotated[float, Field(ge=0, le=9999999.999999)]] = None
    Awkward: Optional[Annotated[str, Field(max_length=1)]] = None
    Two_Man_Lift: Optional[Annotated[str, Field(max_length=1)]] = None
    Decatalogued: Optional[Annotated[str, Field(max_length=1)]] = None
    Stock_Check_Rule_Id: Optional[Annotated[str, Field(max_length=30)]] = None
    Unkitting_Inherit: Optional[Annotated[str, Field(max_length=1)]] = None
    Serial_At_Stock_Check: Optional[Annotated[str, Field(max_length=1)]] = None
    Serial_At_Stock_Adjust: Optional[Annotated[str, Field(max_length=1)]] = None
    Kit_Ship_Components: Optional[Annotated[str, Field(max_length=1)]] = None
    Unallocatable: Optional[Annotated[str, Field(max_length=1)]] = None
    Batch_At_Kitting: Optional[Annotated[str, Field(max_length=1)]] = None
    Serial_Per_Each: Optional[Annotated[int, Field(ge=0, le=99)]] = None
    Vmi_Allow_Allocation: Optional[Annotated[str, Field(max_length=1)]] = None
    Vmi_Allow_Replenish: Optional[Annotated[str, Field(max_length=1)]] = None
    Vmi_Allow_Interfaced: Optional[Annotated[str, Field(max_length=1)]] = None
    Vmi_Allow_Manual: Optional[Annotated[str, Field(max_length=1)]] = None
    Vmi_Aging_Days: Optional[Annotated[int, Field(ge=0, le=999)]] = None
    Vmi_Overstock_Qty: Optional[Annotated[float, Field(ge=0, le=999999999.999999)]] = None
    Scrap_On_Return: Optional[Annotated[str, Field(max_length=1)]] = None
    Nls_Calendar: Optional[Annotated[str, Field(max_length=30)]] = None
    Harmonised_Product_Code: Optional[Annotated[str, Field(max_length=50)]] = None
    Hanging_Garment: Optional[Annotated[str, Field(max_length=1)]] = None
    Conveyable: Optional[Annotated[str, Field(max_length=1)]] = None
    Fragile: Optional[Annotated[str, Field(max_length=1)]] = None
    Gender: Optional[Annotated[str, Field(max_length=1)]] = None
    High_Security: Optional[Annotated[str, Field(max_length=1)]] = None
    Ugly: Optional[Annotated[str, Field(max_length=1)]] = None
    Collatable: Optional[Annotated[str, Field(max_length=1)]] = None
    Ecommerce: Optional[Annotated[str, Field(max_length=1)]] = None
    Promotion: Optional[Annotated[str, Field(max_length=1)]] = None
    Foldable: Optional[Annotated[str, Field(max_length=1)]] = None
    Style: Optional[Annotated[str, Field(max_length=10)]] = None
    Business_Unit_Code: Optional[Annotated[str, Field(max_length=50)]] = None
    Tag_Merge: Optional[Annotated[str, Field(max_length=1)]] = None
    Carrier_Pallet_Mixing: Optional[Annotated[str, Field(max_length=1)]] = None
    No_Alloc_Back_Order: Optional[Annotated[str, Field(max_length=1)]] = None
    Special_Container_Type: Optional[Annotated[str, Field(max_length=15)]] = None
    Disallow_Rdt_Over_Picking: Optional[Annotated[str, Field(max_length=1)]] = None
    Return_Min_Shelf_Life: Optional[Annotated[int, Field(ge=0, le=99999)]] = None
    Collective_Sequence: Optional[Annotated[int, Field(ge=0, le=9999999999)]] = None
    Weigh_At_Grid_Pick: Optional[Annotated[str, Field(max_length=1)]] = None
    Ce_Excise_Product_Code: Optional[Annotated[str, Field(max_length=4)]] = None
    Ce_Degree_Plato: Optional[Annotated[float, Field(ge=0, le=999.99)]] = None
    Ce_Designation_Origin: Optional[Annotated[str, Field(max_length=350)]] = None
    Ce_Density: Optional[Annotated[float, Field(ge=0, le=999.99)]] = None
    Ce_Brand_Name: Optional[Annotated[str, Field(max_length=350)]] = None
    Ce_Alcoholic_Strength: Optional[Annotated[float, Field(ge=0, le=999.99)]] = None
    Ce_Fiscal_Mark: Optional[Annotated[str, Field(max_length=350)]] = None
    Ce_Size_Of_Producer: Optional[Annotated[str, Field(max_length=15)]] = None
    Ce_Commercial_Desc: Optional[Annotated[str, Field(max_length=350)]] = None
    Serial_No_Outbound: Optional[Annotated[str, Field(max_length=1)]] = None
    Full_Pallet_At_Receipt: Optional[Annotated[str, Field(max_length=1)]] = None
    Always_Full_Pallet: Optional[Annotated[str, Field(max_length=1)]] = None
    Sub_Within_Product_Grp: Optional[Annotated[str, Field(max_length=1)]] = None
    Serial_Check_String: Optional[Annotated[str, Field(max_length=20)]] = None
    Carrier_Product_Type: Optional[Annotated[str, Field(max_length=80)]] = None
    Max_Pack_Configs: Optional[Annotated[int, Field(ge=0, le=9999)]] = None
    Parcel_Packing_By_Piece: Optional[Annotated[str, Field(max_length=1)]] = None

    model_config = {
        "str_strip_whitespace": True,
        "extra": "forbid"
    }

    # Validators for Allowed Values
    @field_validator("Record_Type")
    @classmethod
    def record_type_must_be_sku(cls, v: str) -> str:
        if v != "SKU":
            raise ValueError("Record_Type must be 'SKU'")
        return v

    @field_validator("Merge_Action")
    @classmethod
    def merge_action_allowed_values(cls, v: str) -> str:
        if v not in ["A", "U", "D"]:
            raise ValueError("Merge_Action must be 'A', 'U', or 'D'")
        return v

    @field_validator("Qc_Status")
    @classmethod
    def qc_status_allowed_values(cls, v: Optional[str]) -> Optional[str]:
        if v is not None and v not in ["Hold", "Released", "Rejected"]:
            raise ValueError("Qc_Status must be 'Hold', 'Released', or 'Rejected'")
        return v

    @field_validator("Expiry_Reqd", "Split_Lowest", "Condition_Reqd", "Origin_Reqd", 
                    "Serial_At_Pick", "Serial_At_Pack", "Kit_Sku", "Kit_Split", 
                    "Abc_Disable", "Obsolete_Product", "New_Product", "Disallow_Upload",
                    "Manuf_Dstamp_Reqd", "Manuf_Dstamp_Dflt", "Hazmat", "Disallow_Cross_Dock",
                    "Disallow_Merge_Rules", "Pack_Despatch_Repack", "Serial_At_Receipt",
                    "Serial_Valid_Merge", "Serial_No_Reuse", "Ce_Customs_Excise",
                    "Ce_Duty_Stamp", "Capture_Weight", "Weigh_At_Receipt", "Serial_At_Loading",
                    "Serial_At_Kitting", "Serial_At_Unkitting", "Disallow_Clustering",
                    "Breakpack", "Clearable", "Serial_Dynamic_Range", "Expiry_At_Repack",
                    "Udf_At_Repack", "Manufacture_At_Repack", "Repack_By_Piece", "Collective_Mode",
                    "Awkward", "Two_Man_Lift", "Decatalogued", "Unkitting_Inherit",
                    "Serial_At_Stock_Check", "Serial_At_Stock_Adjust", "Kit_Ship_Components",
                    "Unallocatable", "Batch_At_Kitting", "Vmi_Allow_Allocation", "Vmi_Allow_Replenish",
                    "Vmi_Allow_Interfaced", "Vmi_Allow_Manual", "Scrap_On_Return", "Hanging_Garment",
                    "Conveyable", "Fragile", "High_Security", "Ugly", "Collatable", "Ecommerce",
                    "Promotion", "Foldable", "Tag_Merge", "Carrier_Pallet_Mixing", "No_Alloc_Back_Order",
                    "Disallow_Rdt_Over_Picking", "Weigh_At_Grid_Pick", "Serial_No_Outbound",
                    "Full_Pallet_At_Receipt", "Always_Full_Pallet", "Sub_Within_Product_Grp",
                    "Parcel_Packing_By_Piece")
    @classmethod
    def y_n_flags(cls, v: Optional[str], info) -> Optional[str]:
        if v is not None and v not in ["Y", "N"]:
            raise ValueError(f"{info.field_name} must be 'Y' or 'N'")
        return v

    @field_validator("Incub_Rule")
    @classmethod
    def incub_rule_values(cls, v: Optional[str]) -> Optional[str]:
        if v is not None and v not in ["R", "M"]:
            raise ValueError("Incub_Rule must be 'R' or 'M'")
        return v

    @field_validator("Ce_Vat_Code")
    @classmethod
    def ce_vat_code_values(cls, v: Optional[str]) -> Optional[str]:
        if v is not None and v not in ["S", "Z"]:
            raise ValueError("Ce_Vat_Code must be 'S' or 'Z'")
        return v

    @field_validator("Ce_Warehouse_Type")
    @classmethod
    def ce_warehouse_type_values(cls, v: Optional[str]) -> Optional[str]:
        if v is not None and v not in ["C", "E", "N"]:
            raise ValueError("Ce_Warehouse_Type must be 'C', 'E', or 'N'")
        return v

    @field_validator("Gender")
    @classmethod
    def gender_values(cls, v: Optional[str]) -> Optional[str]:
        if v is not None and v not in ["M", "F"]:
            raise ValueError("Gender must be 'M' or 'F'")
        return v

    # Uppercase Validation
    @field_validator("Sku_Id", "Ean", "Product_Group", "Allocation_Group", "Putaway_Group", 
                    "Kitting_Loc_Id", "Handling_Class", "Hazmat_Id", "Upc", "Client_Id", 
                    "User_Def_Type_1", "User_Def_Type_2", "User_Def_Type_3", "User_Def_Type_4", 
                    "User_Def_Type_5", "User_Def_Type_6", "User_Def_Type_7", "User_Def_Type_8", 
                    "Spec_Id", "Ce_Standard_Currency", "Client_Group", "Ce_Commodity_Code", 
                    "Ce_Coo", "Ce_Cwc", "Ce_Product_Type", "Commodity_Code", "Family_Group", 
                    "Stage_Route_Id", "Serial_Format", "Serial_Range", "Stock_Check_Rule_Id", 
                    "Style", "Business_Unit_Code", "Special_Container_Type", "Ce_Excise_Product_Code", 
                    "Ce_Size_Of_Producer", "Serial_Check_String", "Carrier_Product_Type")
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
        "Record_Type": "SKU",
        "Merge_Action": "A",
        "Sku_Id": "SKU12345",
        "Description": "Test Product",
        "Client_Id": "CLIENT1",
        "Qc_Status": "Released",
        "Expiry_Reqd": "Y",
        "Each_Height": 10.5,
        "Each_Weight": 2.3,
        "User_Def_Num_1": 123.456
    }

    try:
        sku = SKU(**valid_data)
        print("Valid data:", sku.model_dump())
    except ValueError as e:
        print("Validation error:", str(e))