from pydantic import BaseModel, Field, field_validator
from typing import Annotated, Optional
from datetime import datetime

class ODH(BaseModel):
    Record_Type: Annotated[str, Field(max_length=3, min_length=3)]
    Merge_Action: Annotated[str, Field(max_length=1, min_length=1)]
    Order_Id: Annotated[str, Field(max_length=20)]
    Order_Type: Optional[Annotated[str, Field(max_length=10)]] = None
    Status: Optional[Annotated[str, Field(max_length=15)]] = None
    Priority: Optional[Annotated[str, Field(max_length=4)]] = None
    Ship_Dock: Optional[Annotated[str, Field(max_length=20)]] = None
    Work_Group: Optional[Annotated[str, Field(max_length=20)]] = None
    Consignment: Optional[Annotated[str, Field(max_length=20)]] = None
    Delivery_Point: Optional[Annotated[str, Field(max_length=15)]] = None
    Load_Sequence: Optional[Annotated[int, Field(le=9999999999)]] = None
    From_Site_Id: Optional[Annotated[str, Field(max_length=10)]] = None
    To_Site_Id: Optional[Annotated[str, Field(max_length=10)]] = None
    Customer_Id: Optional[Annotated[str, Field(max_length=15)]] = None
    Order_Date: Optional[Annotated[str, Field(max_length=14, min_length=14)]] = None
    Ship_By_Date: Optional[Annotated[str, Field(max_length=14, min_length=14)]] = None
    Purchase_Order: Optional[Annotated[str, Field(max_length=25)]] = None
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
    Instructions: Optional[Annotated[str, Field(max_length=180)]] = None
    Repack: Optional[Annotated[str, Field(max_length=1, min_length=1)]] = None
    Owner_Id: Annotated[str, Field(max_length=10)]
    Carrier_Id: Optional[Annotated[str, Field(max_length=25)]] = None
    Dispatch_Method: Optional[Annotated[str, Field(max_length=40)]] = None
    Service_Level: Optional[Annotated[str, Field(max_length=40)]] = None
    Inv_Address_Id: Optional[Annotated[str, Field(max_length=15)]] = None
    Inv_Contact: Optional[Annotated[str, Field(max_length=25)]] = None
    Inv_Contact_Phone: Optional[Annotated[str, Field(max_length=25)]] = None
    Inv_Contact_Fax: Optional[Annotated[str, Field(max_length=25)]] = None
    Inv_Contact_Email: Optional[Annotated[str, Field(max_length=256)]] = None
    Inv_Name: Optional[Annotated[str, Field(max_length=50)]] = None
    Inv_Address1: Optional[Annotated[str, Field(max_length=60)]] = None
    Inv_Address2: Optional[Annotated[str, Field(max_length=60)]] = None
    Inv_Town: Optional[Annotated[str, Field(max_length=60)]] = None
    Inv_County: Optional[Annotated[str, Field(max_length=60)]] = None
    Inv_Postcode: Optional[Annotated[str, Field(max_length=20)]] = None
    Inv_Country: Optional[Annotated[str, Field(max_length=25)]] = None
    Deliver_By_Date: Optional[Annotated[str, Field(max_length=14, min_length=14)]] = None
    Fastest_Carrier: Optional[Annotated[str, Field(max_length=1, min_length=1)]] = None
    Cheapest_Carrier: Optional[Annotated[str, Field(max_length=1, min_length=1)]] = None
    Site_Replen: Optional[Annotated[str, Field(max_length=1, min_length=1)]] = None
    Cid_Number: Optional[Annotated[str, Field(max_length=20)]] = None
    Sid_Number: Optional[Annotated[str, Field(max_length=20)]] = None
    Location_Number: Optional[Annotated[int, Field(le=99999999999999999999)]] = None
    Freight_Charges: Optional[Annotated[str, Field(max_length=10)]] = None
    Client_Id: Annotated[str, Field(max_length=10)]
    Export: Optional[Annotated[str, Field(max_length=1, min_length=1)]] = None
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
    Move_Task_Status: Optional[Annotated[str, Field(max_length=20)]] = None
    Time_Zone_Name: Optional[Annotated[str, Field(max_length=64)]] = None
    Repack_Loc_Id: Optional[Annotated[str, Field(max_length=20)]] = None
    Ce_Reason_Code: Optional[Annotated[str, Field(max_length=10)]] = None
    Ce_Reason_Notes: Optional[Annotated[str, Field(max_length=80)]] = None
    Ce_Order_Type: Optional[Annotated[str, Field(max_length=2)]] = None
    Ce_Customs_Customer: Optional[Annotated[str, Field(max_length=15)]] = None
    Ce_Excise_Customer: Optional[Annotated[str, Field(max_length=15)]] = None
    Ce_Instructions: Optional[Annotated[str, Field(max_length=180)]] = None
    Client_Group: Optional[Annotated[str, Field(max_length=10)]] = None
    Delivered_Dstamp: Optional[Annotated[str, Field(max_length=14, min_length=14)]] = None
    Signatory: Optional[Annotated[str, Field(max_length=25)]] = None
    Route_Id: Optional[Annotated[str, Field(max_length=10)]] = None
    Cross_Dock_To_Site: Optional[Annotated[str, Field(max_length=1, min_length=1)]] = None
    Web_Service_Alloc_Immed: Optional[Annotated[str, Field(max_length=1, min_length=1)]] = None
    Web_Service_Alloc_Clean: Optional[Annotated[str, Field(max_length=1, min_length=1)]] = None
    Disallow_Short_Ship: Optional[Annotated[str, Field(max_length=1, min_length=1)]] = None
    Work_Order_Type: Optional[Annotated[str, Field(max_length=20)]] = None
    Status_Reason_Code: Optional[Annotated[str, Field(max_length=10)]] = None
    Hub_Address_Id: Optional[Annotated[str, Field(max_length=15)]] = None
    Hub_Contact: Optional[Annotated[str, Field(max_length=25)]] = None
    Hub_Contact_Phone: Optional[Annotated[str, Field(max_length=25)]] = None
    Hub_Contact_Fax: Optional[Annotated[str, Field(max_length=25)]] = None
    Hub_Contact_Email: Optional[Annotated[str, Field(max_length=256)]] = None
    Hub_Name: Optional[Annotated[str, Field(max_length=50)]] = None
    Hub_Address1: Optional[Annotated[str, Field(max_length=60)]] = None
    Hub_Address2: Optional[Annotated[str, Field(max_length=60)]] = None
    Hub_Town: Optional[Annotated[str, Field(max_length=60)]] = None
    Hub_County: Optional[Annotated[str, Field(max_length=60)]] = None
    Hub_Postcode: Optional[Annotated[str, Field(max_length=20)]] = None
    Hub_Country: Optional[Annotated[str, Field(max_length=25)]] = None
    Stage_Route_Id: Optional[Annotated[str, Field(max_length=20)]] = None
    Single_Order_Sortation: Optional[Annotated[str, Field(max_length=1, min_length=1)]] = None
    Hub_Carrier_Id: Optional[Annotated[str, Field(max_length=25)]] = None
    Hub_Service_Level: Optional[Annotated[str, Field(max_length=40)]] = None
    Force_Single_Carrier: Optional[Annotated[str, Field(max_length=1, min_length=1)]] = None
    Expected_Value: Optional[Annotated[float, Field(le=999999999999)]] = None
    Expected_Volume: Optional[Annotated[float, Field(le=999999999999999)]] = None
    Expected_Weight: Optional[Annotated[float, Field(le=999999999999999)]] = None
    Tod: Optional[Annotated[str, Field(max_length=3)]] = None
    Tod_Place: Optional[Annotated[str, Field(max_length=60)]] = None
    Language: Optional[Annotated[str, Field(max_length=8)]] = None
    Seller_Name: Optional[Annotated[str, Field(max_length=50)]] = None
    Seller_Phone: Optional[Annotated[str, Field(max_length=25)]] = None
    Documentation_Text_1: Optional[Annotated[str, Field(max_length=180)]] = None
    Documentation_Text_2: Optional[Annotated[str, Field(max_length=180)]] = None
    Documentation_Text_3: Optional[Annotated[str, Field(max_length=180)]] = None
    Cod: Optional[Annotated[str, Field(max_length=1, min_length=1)]] = None
    Cod_Value: Optional[Annotated[float, Field(le=999999999999)]] = None
    Cod_Currency: Optional[Annotated[str, Field(max_length=3)]] = None
    Cod_Type: Optional[Annotated[str, Field(max_length=10)]] = None
    Vat_Number: Optional[Annotated[str, Field(max_length=20)]] = None
    Inv_Vat_Number: Optional[Annotated[str, Field(max_length=20)]] = None
    Hub_Vat_Number: Optional[Annotated[str, Field(max_length=20)]] = None
    Inv_Reference: Optional[Annotated[str, Field(max_length=35)]] = None
    Inv_Dstamp: Optional[Annotated[str, Field(max_length=14, min_length=14)]] = None
    Inv_Currency: Optional[Annotated[str, Field(max_length=3)]] = None
    Print_Invoice: Optional[Annotated[str, Field(max_length=1, min_length=1)]] = None
    Letter_Of_Credit: Optional[Annotated[str, Field(max_length=35)]] = None
    Payment_Terms: Optional[Annotated[str, Field(max_length=35)]] = None
    Subtotal_1: Optional[Annotated[float, Field(le=999999999999)]] = None
    Subtotal_2: Optional[Annotated[float, Field(le=999999999999)]] = None
    Subtotal_3: Optional[Annotated[float, Field(le=999999999999)]] = None
    Subtotal_4: Optional[Annotated[float, Field(le=999999999999)]] = None
    Freight_Cost: Optional[Annotated[float, Field(le=999999999999)]] = None
    Freight_Terms: Optional[Annotated[str, Field(max_length=10)]] = None
    Insurance_Cost: Optional[Annotated[float, Field(le=999999999999)]] = None
    Misc_Charges: Optional[Annotated[float, Field(le=999999999999)]] = None
    Discount: Optional[Annotated[float, Field(le=999999999999)]] = None
    Other_Fee: Optional[Annotated[float, Field(le=999999999999)]] = None
    Inv_Total_1: Optional[Annotated[float, Field(le=999999999999)]] = None
    Inv_Total_2: Optional[Annotated[float, Field(le=999999999999)]] = None
    Inv_Total_3: Optional[Annotated[float, Field(le=999999999999)]] = None
    Inv_Total_4: Optional[Annotated[float, Field(le=999999999999)]] = None
    Tax_Rate_1: Optional[Annotated[float, Field(le=999999999999)]] = None
    Tax_Basis_1: Optional[Annotated[float, Field(le=999999999999)]] = None
    Tax_Amount_1: Optional[Annotated[float, Field(le=999999999999)]] = None
    Tax_Rate_2: Optional[Annotated[float, Field(le=999999999999)]] = None
    Tax_Basis_2: Optional[Annotated[float, Field(le=999999999999)]] = None
    Tax_Amount_2: Optional[Annotated[float, Field(le=999999999999)]] = None
    Tax_Rate_3: Optional[Annotated[float, Field(le=999999999999)]] = None
    Tax_Basis_3: Optional[Annotated[float, Field(le=999999999999)]] = None
    Tax_Amount_3: Optional[Annotated[float, Field(le=999999999999)]] = None
    Tax_Rate_4: Optional[Annotated[float, Field(le=999999999999)]] = None
    Tax_Basis_4: Optional[Annotated[float, Field(le=999999999999)]] = None
    Tax_Amount_4: Optional[Annotated[float, Field(le=999999999999)]] = None
    Tax_Rate_5: Optional[Annotated[float, Field(le=999999999999)]] = None
    Tax_Basis_5: Optional[Annotated[float, Field(le=999999999999)]] = None
    Tax_Amount_5: Optional[Annotated[float, Field(le=999999999999)]] = None
    Order_Reference: Optional[Annotated[str, Field(max_length=35)]] = None
    Start_By_Date: Optional[Annotated[str, Field(max_length=14, min_length=14)]] = None
    Metapack_Carrier_Pre: Optional[Annotated[str, Field(max_length=1, min_length=1)]] = None
    Collective_Mode: Optional[Annotated[str, Field(max_length=1, min_length=1)]] = None
    Contact_Mobile: Optional[Annotated[str, Field(max_length=25)]] = None
    Inv_Contact_Mobile: Optional[Annotated[str, Field(max_length=25)]] = None
    Hub_Contact_Mobile: Optional[Annotated[str, Field(max_length=25)]] = None
    Shipment_Group: Optional[Annotated[str, Field(max_length=20)]] = None
    Freight_Currency: Optional[Annotated[str, Field(max_length=3)]] = None
    Ncts: Optional[Annotated[str, Field(max_length=10)]] = None
    Nls_Calendar: Optional[Annotated[str, Field(max_length=30)]] = None
    Mpack_Consignment: Optional[Annotated[str, Field(max_length=30)]] = None
    Mpack_Nominated_Dstamp: Optional[Annotated[str, Field(max_length=14, min_length=14)]] = None
    Gln: Optional[Annotated[str, Field(max_length=13)]] = None
    Hub_Gln: Optional[Annotated[str, Field(max_length=13)]] = None
    Inv_Gln: Optional[Annotated[str, Field(max_length=13)]] = None
    Allocation_Priority: Optional[Annotated[int, Field(le=9999)]] = None
    Allow_Pallet_Pick: Optional[Annotated[str, Field(max_length=1, min_length=1)]] = None
    Split_Shipping_Units: Optional[Annotated[str, Field(max_length=1, min_length=1)]] = None
    Vol_Pck_Sscc_Label: Optional[Annotated[str, Field(max_length=1, min_length=1)]] = None
    Collective_Sequence: Optional[Annotated[int, Field(le=9999999999)]] = None
    Trax_Use_Hub_Addr: Optional[Annotated[str, Field(max_length=1, min_length=1)]] = None
    Direct_To_Store: Optional[Annotated[str, Field(max_length=1, min_length=1)]] = None
    Vol_Ctr_Label_Format: Optional[Annotated[str, Field(max_length=30)]] = None
    Retailer_Id: Optional[Annotated[str, Field(max_length=15)]] = None
    Carrier_Bags: Optional[Annotated[str, Field(max_length=1, min_length=1)]] = None
    Parcel_Shop_Id: Optional[Annotated[str, Field(max_length=256)]] = None

    model_config = {
        "str_strip_whitespace": True,
        "extra": "forbid"
    }

    # Validators for Allowed Values
    @field_validator("Record_Type")
    @classmethod
    def record_type_must_be_odh(cls, v: str) -> str:
        if v != "ODH":
            raise ValueError("Record_Type must be 'ODH'")
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
        if v is not None and v not in ["Cancelled", "Complete", "Delivered", "Hold", "Released", "Shipped"]:
            raise ValueError("Status must be one of: 'Cancelled', 'Complete', 'Delivered', 'Hold', 'Released', 'Shipped'")
        return v

    @field_validator("Repack", "Fastest_Carrier", "Cheapest_Carrier", "Site_Replen", "Export", 
                     "Disallow_Merge_Rules", "User_Def_Chk_1", "User_Def_Chk_2", "User_Def_Chk_3", 
                     "User_Def_Chk_4", "Print_Invoice", "Metapack_Carrier_Pre", "Collective_Mode", 
                     "Allow_Pallet_Pick", "Split_Shipping_Units", "Vol_Pck_Sscc_Label", "Trax_Use_Hub_Addr", 
                     "Direct_To_Store", "Carrier_Bags", "Single_Order_Sortation", "Force_Single_Carrier", "Cod")
    @classmethod
    def y_n_flags(cls, v: Optional[str], info) -> Optional[str]:
        if v is not None and v not in ["Y", "N"]:
            raise ValueError(f"{info.field_name} must be 'Y' or 'N'")
        return v

    @field_validator("Disallow_Short_Ship")
    @classmethod
    def disallow_short_ship_values(cls, v: Optional[str]) -> Optional[str]:
        if v is not None and v not in ["F", "P"]:
            raise ValueError("Disallow_Short_Ship must be 'F' or 'P'")
        return v

    @field_validator("Freight_Charges")
    @classmethod
    def freight_charges_values(cls, v: Optional[str]) -> Optional[str]:
        if v is not None and v not in ["Prepaid", "Collect", "3rd Party"]:
            raise ValueError("Freight_Charges must be 'Prepaid', 'Collect', or '3rd Party'")
        return v

    @field_validator("Work_Order_Type")
    @classmethod
    def work_order_type_values(cls, v: Optional[str]) -> Optional[str]:
        if v is not None and v not in ["kittostock", "unkittostock", ""]:
            raise ValueError("Work_Order_Type must be 'kittostock', 'unkittostock', or blank")
        return v

    @field_validator("Move_Task_Status")
    @classmethod
    def move_task_status_values(cls, v: Optional[str]) -> Optional[str]:
        if v is not None and v not in ["Hold", "Released"]:
            raise ValueError("Move_Task_Status must be 'Hold' or 'Released'")
        return v

    # Uppercase Validation
    @field_validator("Order_Id", "Order_Type", "Priority", "Ship_Dock", "Work_Group", "Consignment", 
                     "Delivery_Point", "From_Site_Id", "To_Site_Id", "Customer_Id", "Purchase_Order", 
                     "Postcode", "Country", "Owner_Id", "Carrier_Id", "Dispatch_Method", "Service_Level", 
                     "Inv_Address_Id", "Inv_Postcode", "Inv_Country", "Cid_Number", "Sid_Number", 
                     "Client_Id", "User_Def_Type_1", "User_Def_Type_2", "User_Def_Type_3", 
                     "User_Def_Type_4", "User_Def_Type_5", "User_Def_Type_6", "User_Def_Type_7", 
                     "User_Def_Type_8", "Soh_Id", "Repack_Loc_Id", "Ce_Reason_Code", "Ce_Order_Type", 
                     "Ce_Customs_Customer", "Ce_Excise_Customer", "Client_Group", "Route_Id", 
                     "Status_Reason_Code", "Hub_Address_Id", "Hub_Postcode", "Hub_Country", 
                     "Stage_Route_Id", "Hub_Carrier_Id", "Hub_Service_Level", "Order_Reference", 
                     "Shipment_Group", "Freight_Currency", "Ncts", "Mpack_Consignment", "Gln", 
                     "Hub_Gln", "Inv_Gln", "Vol_Ctr_Label_Format", "Retailer_Id", "Tod", "Language")
    @classmethod
    def enforce_uppercase(cls, v: Optional[str], info) -> Optional[str]:
        if v is not None and v != '' and not v.isupper():
            v = v.upper()
        return v

    # Date Format Validation
    @field_validator("Order_Date", "Ship_By_Date", "Deliver_By_Date", "User_Def_Date_1", 
                     "User_Def_Date_2", "User_Def_Date_3", "User_Def_Date_4", "Delivered_Dstamp", 
                     "Inv_Dstamp", "Start_By_Date", "Mpack_Nominated_Dstamp")
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
            raise ValueError(f"{info.field_name} {v} must be between 0 and 9999999999")
        return v

    @field_validator("Location_Number")
    @classmethod
    def validate_location_number(cls, v: Optional[int], info) -> Optional[int]:
        if v is not None and (v < 0 or v > 99999999999999999999):
            raise ValueError(f"{info.field_name} must be between 0 and 99999999999999999999")
        return v

    @field_validator("Allocation_Priority")
    @classmethod
    def validate_allocation_priority(cls, v: Optional[int], info) -> Optional[int]:
        if v is not None and (v < 0 or v > 9999):
            raise ValueError(f"{info.field_name} must be between 0 and 9999")
        return v

    @field_validator("User_Def_Num_1", "User_Def_Num_2", "User_Def_Num_3", "User_Def_Num_4", 
                     "Expected_Volume", "Expected_Weight")
    @classmethod
    def validate_decimal_15(cls, v: Optional[float], info) -> Optional[float]:
        if v is not None and (v < -999999999999999 or v > 999999999999999):
            raise ValueError(f"{info.field_name} must be between -999999999999999 and 999999999999999")
        return v

    @field_validator("Expected_Value", "Cod_Value", "Subtotal_1", "Subtotal_2", "Subtotal_3", 
                     "Subtotal_4", "Freight_Cost", "Insurance_Cost", "Misc_Charges", "Discount", 
                     "Other_Fee", "Inv_Total_1", "Inv_Total_2", "Inv_Total_3", "Inv_Total_4", 
                     "Tax_Rate_1", "Tax_Basis_1", "Tax_Amount_1", "Tax_Rate_2", "Tax_Basis_2", 
                     "Tax_Amount_2", "Tax_Rate_3", "Tax_Basis_3", "Tax_Amount_3", "Tax_Rate_4", 
                     "Tax_Basis_4", "Tax_Amount_4", "Tax_Rate_5", "Tax_Basis_5", "Tax_Amount_5")
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
        "Owner_Id": "OWN123",
        "Client_Id": "CLI123",
        "Status": "Delivered",
        "Order_Date": "20230305143000",
        "Repack": "Y",
        "User_Def_Num_1": 12345.6789
    }

    try:
        order = ODH(**valid_data)
        print("Valid data:", order.model_dump())
    except ValueError as e:
        print("Validation error:", str(e))
