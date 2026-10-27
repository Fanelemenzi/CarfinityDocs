# Database Schema Documentation

## Project Overview
This document outlines the complete database schema for the Vehicle Management System, which includes vehicle tracking, maintenance management, insurance assessments, inspections, and organizational management.

## Table of Contents
1. [Core Vehicle Management](#core-vehicle-management)
2. [User Management](#user-management)
3. [Organization Management](#organization-management)
4. [Maintenance System](#maintenance-system)
5. [Maintenance History & Inspections](#maintenance-history--inspections)
6. [Vehicle Equipment & Specifications](#vehicle-equipment--specifications)
7. [Assessment System](#assessment-system)
8. [Insurance Management](#insurance-management)
9. [Notifications & Alerts](#notifications--alerts)
10. [Onboarding System](#onboarding-system)
11. [Relationships Overview](#relationships-overview)

---

## Core Vehicle Management

### vehicles_vehicle
**Primary vehicle information table**

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | AutoField | PRIMARY KEY | Auto-incrementing primary key |
| vin | CharField(20) | UNIQUE, NOT NULL | Vehicle Identification Number |
| make | CharField(50) | NOT NULL | Vehicle manufacturer |
| model | CharField(50) | NOT NULL | Vehicle model |
| manufacture_year | PositiveIntegerField | NOT NULL | Year of manufacture |
| body_type | CharField(20) | NULL | Vehicle body type |
| engine_code | CharField(20) | NULL | Engine identification code |
| interior_color | CharField(30) | NULL | Interior color |
| exterior_color | CharField(30) | NULL | Exterior color |
| purchase_date | DateField | NULL | Date of purchase |
| license_plate | CharField(20) | NULL | License plate number |
| fuel_type | CharField(50) | NULL | Type of fuel |
| transmission_type | CharField(50) | NULL | Transmission type |
| powertrain_displacement | CharField(50) | NULL | Engine displacement |
| powertrain_power | CharField(5) | NULL | Engine power |
| plant_location | CharField(50) | NULL | Manufacturing plant location |
| created_at | DateTimeField | AUTO_NOW_ADD | Record creation timestamp |
| updated_at | DateTimeField | AUTO_NOW | Record update timestamp |

**Properties:**
- `current_mileage`: Latest mileage from maintenance/inspection records
- `health_score`: Latest vehicle health score from inspections
- `health_status`: Vehicle health status (Healthy/Needs Attention/Critical)

### vehicles_vehicleownership
**Vehicle ownership tracking**

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | AutoField | PRIMARY KEY | Auto-incrementing primary key |
| vehicle_id | ForeignKey | NOT NULL | Reference to vehicles_vehicle |
| user_id | ForeignKey | NOT NULL | Reference to auth_user |
| start_date | DateField | NOT NULL | Ownership start date |
| end_date | DateField | NULL | Ownership end date |
| is_current_owner | BooleanField | DEFAULT TRUE | Current ownership status |

### vehicles_vehiclestatus
**Vehicle status information (accidents, fraud, theft)**

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| vehicle_id | OneToOneField | PRIMARY KEY | Reference to vehicles_vehicle |
| accident_history | CharField(30) | DEFAULT 'NHA' | Accident history status |
| odometer_fraud | CharField(30) | DEFAULT 'NOF' | Odometer fraud status |
| theft_involvement | CharField(30) | DEFAULT 'NHT' | Theft involvement status |
| legal_status | CharField(30) | DEFAULT 'LG' | Legal status |
| owner_history | IntegerField | DEFAULT 0 | Number of previous owners |

**Choices:**
- accident_history: NHA (No History), OIIA (Once Involved), CAD (Currently Damaged)
- odometer_fraud: NOF (No Fraud), SOF (Suspected Fraud)
- theft_involvement: NHT (No History), OIT (Once Involved), STI (Suspected)
- legal_status: LG (Looks Good), ILA (Involved Legal Action)

### vehicles_vehiclehistory
**Detailed vehicle history events**

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | AutoField | PRIMARY KEY | Auto-incrementing primary key |
| vehicle_id | ForeignKey | NULL | Reference to vehicles_vehicle |
| owner_history | IntegerField | DEFAULT 0 | Number of previous owners |
| event_type | CharField(50) | NULL | Type of event |
| event_date | DateField | NULL | Date of event |
| reported_date | DateField | NULL | Date event was reported |
| description | TextField | NULL | Event description |
| reported_by_id | ForeignKey | NULL | User who reported event |
| verified | BooleanField | DEFAULT FALSE | Verification status |
| verified_by_id | ForeignKey | NULL | User who verified event |
| verified_at | DateTimeField | NULL | Verification timestamp |
| accident_severity | CharField(50) | NULL | Accident severity level |
| accident_location | CharField(255) | NULL | Accident location |
| police_report_number | CharField(100) | NULL | Police report number |
| insurance_claim_number | CharField(100) | NULL | Insurance claim number |
| odometer_reading | PositiveIntegerField | NULL | Odometer reading at event |
| fraud_type | CharField(50) | NULL | Type of fraud |
| reported_mileage | PositiveIntegerField | NULL | Reported mileage |
| theft_location | CharField(255) | NULL | Theft location |
| recovery_date | DateField | NULL | Recovery date |
| recovery_location | CharField(255) | NULL | Recovery location |
| damage_during_theft | TextField | NULL | Damage description |
| notes | TextField | NULL | Additional notes |
| created_at | DateTimeField | AUTO_NOW_ADD | Record creation timestamp |
| updated_at | DateTimeField | AUTO_NOW | Record update timestamp |

**Event Types:**
- ACCIDENT, ODOMETER_FRAUD, THEFT, RECALL, REPAIR, OTHER

### vehicles_vehicleimage
**Vehicle image storage**

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | AutoField | PRIMARY KEY | Auto-incrementing primary key |
| vehicle_id | ForeignKey | NOT NULL | Reference to vehicles_vehicle |
| image | ImageField | NOT NULL | Image file |
| image_type | CharField(20) | NOT NULL | Type of image |
| description | CharField(255) | NULL | Image description |
| uploaded_by_id | ForeignKey | NULL | User who uploaded image |
| uploaded_at | DateTimeField | AUTO_NOW_ADD | Upload timestamp |
| is_primary | BooleanField | DEFAULT FALSE | Primary image flag |

**Image Types:**
- FRONT, REAR, SIDE_LEFT, SIDE_RIGHT, INTERIOR, ENGINE, DASHBOARD, TRUNK, WHEELS, DAMAGE, DOCUMENTS, OTHER

### vehicles_vehiclevaluation
**Vehicle valuation information**

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| vehicle_id | OneToOneField | PRIMARY KEY | Reference to vehicles_vehicle |
| estimated_value | DecimalField(10,2) | NOT NULL | Estimated market value |
| condition_rating | CharField(20) | NOT NULL | Vehicle condition rating |
| valuation_source | CharField(20) | NOT NULL | Source of valuation |
| last_updated | DateTimeField | AUTO_NOW | Last update timestamp |
| mileage_at_valuation | PositiveIntegerField | NULL | Mileage when valued |
| valuation_notes | TextField | NULL | Valuation notes |
| created_at | DateTimeField | AUTO_NOW_ADD | Record creation timestamp |
| updated_at | DateTimeField | AUTO_NOW | Record update timestamp |

---

## User Management

### users_profile
**Extended user profile information**

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | AutoField | PRIMARY KEY | Auto-incrementing primary key |
| user_id | OneToOneField | NOT NULL | Reference to auth_user |
| address | CharField(255) | NULL | User address |
| city | CharField(100) | NULL | City |
| state | CharField(100) | NULL | State/Province |
| country | CharField(100) | NULL | Country |
| postal_code | CharField(20) | NULL | Postal/ZIP code |
| profile_picture | ImageField | NULL | Profile picture |
| date_of_birth | DateField | NULL | Date of birth |
| preferred_language | CharField(10) | DEFAULT 'en' | Preferred language |

### users_role
**System roles definition**

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | AutoField | PRIMARY KEY | Auto-incrementing primary key |
| name | CharField(100) | UNIQUE, NOT NULL | Role name |
| description | TextField | NULL | Role description |
| permissions | JSONField | DEFAULT {} | Role permissions |

### users_userrole
**User role assignments**

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | AutoField | PRIMARY KEY | Auto-incrementing primary key |
| user_id | ForeignKey | NOT NULL | Reference to auth_user |
| role_id | ForeignKey | NOT NULL | Reference to users_role |
| assigned_at | DateTimeField | AUTO_NOW_ADD | Assignment timestamp |

**Constraints:**
- UNIQUE(user_id, role_id)

### users_dataconsent
**User data consent tracking**

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | AutoField | PRIMARY KEY | Auto-incrementing primary key |
| user_id | ForeignKey | NOT NULL | Reference to auth_user |
| consent_type | CharField(100) | NOT NULL | Type of consent |
| granted_at | DateTimeField | AUTO_NOW_ADD | Consent granted timestamp |
| revoked_at | DateTimeField | NULL | Consent revoked timestamp |

**Consent Types:**
- PRIVACY, EMAIL, DATA, DATA_ANALYTICS

---

## Organization Management

### organizations_organization
**Organization information**

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | AutoField | PRIMARY KEY | Auto-incrementing primary key |
| name | CharField(255) | NOT NULL | Organization name |
| organization_type | CharField(20) | DEFAULT 'other' | Organization type |
| address | CharField(255) | NULL | Organization address |
| city | CharField(100) | NULL | City |
| state | CharField(100) | NULL | State/Province |
| country | CharField(100) | NULL | Country |
| postal_code | CharField(20) | NULL | Postal code |
| contact_email | EmailField | NULL | Contact email |
| contact_phone | CharField(15) | NULL | Contact phone |
| is_insurance_provider | BooleanField | DEFAULT FALSE | Insurance provider flag |
| insurance_license_number | CharField(100) | NULL | Insurance license number |
| insurance_rating | CharField(10) | NULL | Insurance rating |
| created_at | DateTimeField | AUTO_NOW_ADD | Record creation timestamp |
| updated_at | DateTimeField | AUTO_NOW | Record update timestamp |

**Organization Types:**
- insurance, fleet, dealership, service, other

### organizations_organizationuser
**Organization membership**

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | AutoField | PRIMARY KEY | Auto-incrementing primary key |
| user_id | ForeignKey | NOT NULL | Reference to auth_user |
| organization_id | ForeignKey | NOT NULL | Reference to organizations_organization |
| role | CharField(50) | NOT NULL | User role in organization |
| joined_at | DateTimeField | AUTO_NOW_ADD | Join timestamp |
| is_active | BooleanField | DEFAULT TRUE | Active membership status |
| created_at | DateTimeField | AUTO_NOW_ADD | Record creation timestamp |
| updated_at | DateTimeField | AUTO_NOW | Record update timestamp |

**Roles:**
- ADMIN, MANAGER, DRIVER, AGENT, UNDERWRITER, CLAIMS_ADJUSTER

### organizations_organizationvehicle
**Organization vehicle assignments**

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | AutoField | PRIMARY KEY | Auto-incrementing primary key |
| vehicle_id | ForeignKey | NOT NULL | Reference to vehicles_vehicle |
| organization_id | ForeignKey | NOT NULL | Reference to organizations_organization |
| assigned_to_id | ForeignKey | NULL | User assigned to vehicle |
| assigned_at | DateTimeField | NULL | Assignment timestamp |
| is_active | BooleanField | DEFAULT TRUE | Active assignment status |
| created_at | DateTimeField | AUTO_NOW_ADD | Record creation timestamp |
| updated_at | DateTimeField | AUTO_NOW | Record update timestamp |

### organizations_insuranceorganization
**Insurance-specific organization details**

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| organization_id | OneToOneField | PRIMARY KEY | Reference to organizations_organization |
| naic_number | CharField(20) | NULL | NAIC company code |
| am_best_rating | CharField(10) | NULL | A.M. Best rating |
| states_licensed | TextField | NULL | Licensed states |
| total_policies | IntegerField | DEFAULT 0 | Total policies count |
| total_premium_volume | DecimalField(15,2) | DEFAULT 0 | Total premium volume |
| max_risk_score_threshold | FloatField | DEFAULT 7.0 | Max acceptable risk score |
| auto_approve_low_risk | BooleanField | DEFAULT TRUE | Auto-approve low risk |
| require_inspection_threshold | FloatField | DEFAULT 5.0 | Inspection requirement threshold |
| send_maintenance_alerts | BooleanField | DEFAULT TRUE | Send maintenance alerts |
| send_risk_alerts | BooleanField | DEFAULT TRUE | Send risk alerts |
| alert_email | EmailField | NULL | Alert email address |
| created_at | DateTimeField | AUTO_NOW_ADD | Record creation timestamp |
| updated_at | DateTimeField | AUTO_NOW | Record update timestamp |

---

## Maintenance System

### maintenance_servicetype
**Service type definitions**

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | AutoField | PRIMARY KEY | Auto-incrementing primary key |
| name | CharField(100) | NOT NULL | Service type name |
| description | TextField | NULL | Service description |
| recommended_interval_mileage | PositiveIntegerField | NULL | Recommended mileage interval |
| recommended_interval_time | CharField(50) | NULL | Recommended time interval |
| created_at | DateTimeField | AUTO_NOW_ADD | Record creation timestamp |
| updated_at | DateTimeField | AUTO_NOW | Record update timestamp |

### maintenance_part
**Parts inventory**

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | AutoField | PRIMARY KEY | Auto-incrementing primary key |
| name | CharField(100) | NOT NULL | Part name |
| description | TextField | NULL | Part description |
| manufacturer | CharField(100) | NULL | Manufacturer |
| part_number | CharField(100) | NULL | Part number |
| cost | DecimalField(10,2) | NULL | Part cost |
| stock_quantity | PositiveIntegerField | DEFAULT 0 | Stock quantity |
| minimum_stock_level | PositiveIntegerField | DEFAULT 5 | Minimum stock level |
| category | CharField(100) | NULL | Part category |
| created_at | DateTimeField | AUTO_NOW_ADD | Record creation timestamp |
| updated_at | DateTimeField | AUTO_NOW | Record update timestamp |

### maintenance_maintenanceplan
**Maintenance plan templates**

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | AutoField | PRIMARY KEY | Auto-incrementing primary key |
| name | CharField(100) | NOT NULL | Plan name |
| vehicle_model | CharField(50) | NOT NULL | Vehicle model |
| description | TextField | NULL | Plan description |
| is_active | BooleanField | DEFAULT TRUE | Active status |
| created_at | DateTimeField | AUTO_NOW_ADD | Record creation timestamp |

### maintenance_maintenancetask
**Individual maintenance tasks**

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | AutoField | PRIMARY KEY | Auto-incrementing primary key |
| plan_id | ForeignKey | NOT NULL | Reference to maintenance_maintenanceplan |
| name | CharField(100) | NOT NULL | Task name |
| description | TextField | NULL | Task description |
| service_type_id | ForeignKey | NOT NULL | Reference to maintenance_servicetype |
| interval_miles | PositiveIntegerField | NOT NULL | Mileage interval |
| interval_months | PositiveIntegerField | NOT NULL | Time interval (months) |
| estimated_time | DurationField | NOT NULL | Estimated duration |
| priority | CharField(10) | DEFAULT 'MEDIUM' | Task priority |

**Priority Levels:**
- LOW, MEDIUM, HIGH

### maintenance_taskpartrequirement
**Parts required for tasks**

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | AutoField | PRIMARY KEY | Auto-incrementing primary key |
| task_id | ForeignKey | NOT NULL | Reference to maintenance_maintenancetask |
| part_id | ForeignKey | NOT NULL | Reference to maintenance_part |
| quantity | PositiveIntegerField | DEFAULT 1 | Required quantity |
| notes | CharField(200) | NULL | Additional notes |

### maintenance_assignedvehicleplan
**Vehicle-specific maintenance plan assignments**

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | AutoField | PRIMARY KEY | Auto-incrementing primary key |
| vehicle_id | ForeignKey | NOT NULL | Reference to vehicles_vehicle |
| plan_id | ForeignKey | NOT NULL | Reference to maintenance_maintenanceplan |
| owner_id | ForeignKey | NOT NULL | Reference to auth_user |
| start_date | DateField | NOT NULL | Plan start date |
| current_mileage | PositiveIntegerField | NOT NULL | Current mileage |
| is_active | BooleanField | DEFAULT TRUE | Active status |

### maintenance_scheduledmaintenance
**Scheduled maintenance events**

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | AutoField | PRIMARY KEY | Auto-incrementing primary key |
| assigned_plan_id | ForeignKey | NOT NULL | Reference to maintenance_assignedvehicleplan |
| task_id | ForeignKey | NOT NULL | Reference to maintenance_maintenancetask |
| due_date | DateField | NOT NULL | Due date |
| due_mileage | PositiveIntegerField | NOT NULL | Due mileage |
| status | CharField(20) | DEFAULT 'PENDING' | Maintenance status |
| completed_date | DateField | NULL | Completion date |
| completed_mileage | PositiveIntegerField | NULL | Completion mileage |
| notes | TextField | NULL | Notes |
| technician_id | ForeignKey | NULL | Reference to auth_user |

**Status Options:**
- PENDING, COMPLETED, OVERDUE, SKIPPED

### maintenance_document
**Maintenance documentation**

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | AutoField | PRIMARY KEY | Auto-incrementing primary key |
| maintenance_record_id | ForeignKey | NOT NULL | Reference to maintenance_scheduledmaintenance |
| file_url | URLField | NOT NULL | Document URL |
| document_type | CharField(50) | NOT NULL | Document type |
| uploaded_at | DateTimeField | AUTO_NOW_ADD | Upload timestamp |

---

## Maintenance History & Inspections

### maintenance_history_maintenancerecord
**Completed maintenance records**

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | AutoField | PRIMARY KEY | Auto-incrementing primary key |
| vehicle_id | ForeignKey | NOT NULL | Reference to vehicles_vehicle |
| technician_id | ForeignKey | NULL | Reference to auth_user |
| scheduled_maintenance_id | ForeignKey | NULL | Reference to maintenance_scheduledmaintenance |
| work_done | TextField | NOT NULL | Work performed description |
| date_performed | DateTimeField | DEFAULT NOW | Service date/time |
| mileage | PositiveIntegerField | NOT NULL | Vehicle mileage at service |
| notes | TextField | NULL | Additional notes |
| service_provider | CharField(255) | NULL | Service provider name |
| cost | DecimalField(10,2) | NULL | Total service cost |
| parts_replaced | TextField | NULL | Parts replaced description |
| service_image | ImageField | NULL | Service proof image |
| image_type | CharField(20) | NULL | Image type |
| image_description | CharField(255) | NULL | Image description |
| created_at | DateTimeField | AUTO_NOW_ADD | Record creation timestamp |
| updated_at | DateTimeField | AUTO_NOW | Record update timestamp |

**Image Types:**
- before, during, after, parts, tools, damage, repair, completion, other

### maintenance_history_partusage
**Parts used in maintenance**

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | AutoField | PRIMARY KEY | Auto-incrementing primary key |
| maintenance_record_id | ForeignKey | NOT NULL | Reference to maintenance_history_maintenancerecord |
| part_id | ForeignKey | NOT NULL | Reference to maintenance_part |
| quantity | PositiveIntegerField | DEFAULT 1 | Quantity used |
| unit_cost | DecimalField(8,2) | NULL | Cost per unit |

**Constraints:**
- UNIQUE(maintenance_record_id, part_id)

### maintenance_history_inspection
**Vehicle inspection records**

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | AutoField | PRIMARY KEY | Auto-incrementing primary key |
| vehicle_id | ForeignKey | NOT NULL | Reference to vehicles_vehicle |
| inspection_number | CharField(20) | UNIQUE, NOT NULL | Inspection number |
| year | IntegerField | NOT NULL | Inspection year |
| inspection_result | CharField(30) | NOT NULL | Inspection result |
| vehicle_health_index | CharField(50) | NULL | Health index score |
| inspection_date | DateField | NOT NULL | Inspection date |
| link_to_results | URLField | NULL | External results link |
| inspection_pdf | FileField | NULL | Inspection report PDF |
| pdf_uploaded_at | DateTimeField | NULL | PDF upload timestamp |
| pdf_file_size | PositiveIntegerField | NULL | PDF file size |
| created_at | DateTimeField | NULL | Record creation timestamp |
| updated_at | DateTimeField | NULL | Record update timestamp |

**Inspection Results:**
- PAS (Passed), PMD (Passed with minor defects), PJD (Passed with major defects)
- FMD (Failed minor defects), FJD (Failed major defects), FAI (Failed)

### maintenance_history_inspections
**50-Point quarterly inspection checklist**

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| inspection_id | OneToOneField | PRIMARY KEY | Reference to maintenance_history_inspection |
| technician_id | ForeignKey | NULL | Reference to auth_user |
| inspection_date | DateTimeField | DEFAULT NOW | Inspection date/time |
| mileage_at_inspection | PositiveIntegerField | NOT NULL | Vehicle mileage |

**Inspection Points (50 fields):**
- Engine & Powertrain (10 points): engine_oil_level, oil_filter_condition, coolant_level, etc.
- Electrical & Battery (5 points): battery_voltage, battery_terminals, alternator_output, etc.
- Brakes & Suspension (7 points): brake_pads, brake_discs, brake_fluid, etc.
- Steering & Tires (6 points): steering_response, tire_tread_depth, tire_pressure, etc.
- Exhaust & Emissions (3 points): exhaust_system, catalytic_converter, etc.
- Safety Equipment (5 points): seat_belts, airbags, horn_function, etc.
- Lighting & Visibility (8 points): headlights, brake_lights, windshield, etc.
- HVAC & Interior (4 points): air_conditioning, ventilation, etc.
- Technology & Driver Assist (2 points): infotainment_system, rear_view_camera

**Additional Fields:**
- Section notes fields (9 fields): engine_notes, electrical_notes, etc.
- overall_notes, recommendations
- is_completed, completed_at
- created_at, updated_at

**Status Options for each point:**
- pass, fail, na, minor, major

### maintenance_history_initialinspection
**160-Point initial vehicle inspection**

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | AutoField | PRIMARY KEY | Auto-incrementing primary key |
| vehicle_id | ForeignKey | NOT NULL | Reference to vehicles_vehicle |
| inspection_number | CharField(20) | UNIQUE, NOT NULL | Inspection number |
| technician_id | ForeignKey | NULL | Reference to auth_user |
| inspection_date | DateTimeField | DEFAULT NOW | Inspection date/time |
| mileage_at_inspection | PositiveIntegerField | NOT NULL | Vehicle mileage |

**Inspection Sections:**
1. **Road Test (33 points)**: cold_engine_operation, throttle_operation, brake_vibrations, etc.
2. **Engine Bay (27 points)**: engine_condition, fluid_levels, belt_condition, etc.
3. **Interior (25 points)**: seat_condition, dashboard_function, electronics, etc.
4. **Exterior (25 points)**: body_condition, paint_quality, glass_condition, etc.
5. **Undercarriage (25 points)**: suspension_components, exhaust_system, etc.
6. **Electrical Systems (25 points)**: lighting, charging_system, etc.

**Status Options:**
- pass, fail, na, minor, major, needs_attention

---

## Vehicle Equipment & Specifications

### vehicle_equip_powertrainanddrivetrain
**Powertrain and drivetrain specifications**

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| vehicle_id | OneToOneField | PRIMARY KEY | Reference to vehicles_vehicle |
| base_engine | CharField(100) | NULL | Base engine type |
| engine_displacement | DecimalField(3,1) | NULL | Engine displacement (L) |
| engine_power | PositiveIntegerField | NULL | Engine power (HP) |
| transmission_specifications | CharField(100) | NULL | Transmission specs |
| transmission_type | CharField(3) | NULL | Transmission type |
| gear_count | PositiveSmallIntegerField | NULL | Number of gears |
| drive_layout | CharField(3) | NOT NULL | Drive configuration |
| fuel_system | CharField(1) | NOT NULL | Fuel system type |
| emissions_standard | CharField(4) | NOT NULL | Emissions standard |
| has_start_stop | BooleanField | DEFAULT FALSE | Start-stop system |
| has_regenerative_braking | BooleanField | DEFAULT FALSE | Regenerative braking |
| gearshift_position | CharField(1) | NOT NULL | Gearshift location |
| gearshift_material | CharField(50) | NULL | Gearshift material |
| notes | TextField | NULL | Additional notes |

**Transmission Types:**
- MT (Manual), AT (Automatic), CVT, DCT (Dual-Clutch), AMT (Automated Manual)

**Drive Layouts:**
- FWD (Front-Wheel), RWD (Rear-Wheel), AWD (All-Wheel), 4WD (Four-Wheel)

**Fuel Types:**
- G (Gasoline), D (Diesel), E (Electric), H (Hybrid), P (Plug-in Hybrid), F (Fuel Cell)

### vehicle_equip_chassissuspensionandbraking
**Chassis, suspension, and braking systems**

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| vehicle_id | OneToOneField | PRIMARY KEY | Reference to vehicles_vehicle |
| front_suspension | CharField(4) | NOT NULL | Front suspension type |
| rear_suspension | CharField(4) | NOT NULL | Rear suspension type |
| front_brake_type | CharField(4) | NOT NULL | Front brake type |
| rear_brake_type | CharField(4) | NOT NULL | Rear brake type |
| brake_systems | CharField(5) | NOT NULL | Primary brake system |
| parking_brake_type | CharField(5) | NOT NULL | Parking brake type |
| steering_system | CharField(6) | NOT NULL | Steering system type |
| steering_wheel_features | CharField(30) | NOT NULL | Steering wheel features |
| has_park_distance_control | BooleanField | DEFAULT FALSE | Park distance control |

**Suspension Types:**
- MACP (MacPherson), DUBL (Double Wishbone), MULT (Multi-Link), LEAF, AIR, ADAP (Adaptive)

**Brake Types:**
- DISC, DRUM, CERM (Ceramic), CARB (Carbon Ceramic)

### vehicle_equip_electricalsystem
**Electrical system specifications**

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| vehicle_id | OneToOneField | PRIMARY KEY | Reference to vehicles_vehicle |
| primary_battery_type | CharField(4) | NOT NULL | Primary battery type |
| primary_battery_capacity | PositiveIntegerField | NOT NULL | Primary battery capacity (Ah) |
| has_second_battery | BooleanField | DEFAULT FALSE | Second battery present |
| second_battery_type | CharField(4) | NULL | Second battery type |
| second_battery_capacity | PositiveIntegerField | NULL | Second battery capacity |
| alternator_output | PositiveIntegerField | NOT NULL | Alternator output (A) |
| operating_voltage | PositiveIntegerField | DEFAULT 12 | Operating voltage |
| headlight_type | CharField(6) | NOT NULL | Headlight type |
| headlight_control | BooleanField | DEFAULT FALSE | Auto headlight control |
| headlight_range_control | BooleanField | DEFAULT FALSE | Auto range control |
| instrument_cluster_type | CharField(20) | NOT NULL | Instrument cluster type |
| socket_type | CharField(20) | NOT NULL | Primary socket type |
| horn_type | CharField(6) | NOT NULL | Horn type |

**Battery Types:**
- FLA (Flooded Lead Acid), AGM, GEL, LITH (Lithium-Ion), EFB (Enhanced Flooded)

**Headlight Types:**
- HALO (Halogen), HID (Xenon), LED, LASER, MATRIX

### vehicle_equip_exteriorfeaturesandbody
**Exterior features and body specifications**

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| vehicle_id | OneToOneField | PRIMARY KEY | Reference to vehicles_vehicle |
| body_style | CharField(5) | NOT NULL | Body style |
| windshield_type | CharField(4) | NOT NULL | Windshield glass type |
| side_windows_type | CharField(4) | NOT NULL | Side/rear windows type |
| has_chrome_package | BooleanField | DEFAULT FALSE | Chrome package |
| has_roof_rails | BooleanField | DEFAULT FALSE | Roof rails |
| roof_type | CharField(5) | NOT NULL | Roof type |
| has_front_fog_lamp | BooleanField | DEFAULT FALSE | Front fog lamps |
| has_rear_fog_lamp | BooleanField | DEFAULT FALSE | Rear fog lamp |
| wheel_type | CharField(6) | NOT NULL | Wheel material |
| has_spare_wheel | BooleanField | DEFAULT FALSE | Spare wheel |
| has_trailer_hitch | BooleanField | DEFAULT FALSE | Trailer hitch |
| tailgate_lock_type | CharField(4) | NOT NULL | Tailgate lock type |
| left_mirror_type | CharField(4) | NOT NULL | Left mirror type |
| right_mirror_type | CharField(4) | NOT NULL | Right mirror type |
| antenna_type | CharField(5) | NOT NULL | Antenna type |

**Body Styles:**
- SEDAN, COUPE, HATCH, SUV, TRUCK, VAN, CONV (Convertible), WAGON

### vehicle_equip_activesafetyandadas
**Active safety and ADAS features**

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| vehicle_id | OneToOneField | PRIMARY KEY | Reference to vehicles_vehicle |
| cruise_control_system | CharField(4) | DEFAULT 'NONE' | Cruise control type |
| has_speed_limiter | BooleanField | DEFAULT FALSE | Speed limiter |
| park_distance_control | CharField(4) | DEFAULT 'NONE' | Park assist type |
| driver_alert_system | CharField(6) | DEFAULT 'NONE' | Driver alert system |
| tire_pressure_monitoring | CharField(4) | DEFAULT 'NONE' | TPMS type |
| lane_assist_system | CharField(4) | DEFAULT 'NONE' | Lane assist type |
| blind_spot_monitoring | CharField(4) | DEFAULT 'NONE' | Blind spot monitor |
| collision_warning_system | CharField(4) | DEFAULT 'NONE' | Collision warning |
| has_cross_traffic_alert | BooleanField | DEFAULT FALSE | Cross traffic alert |
| has_traffic_sign_recognition | BooleanField | DEFAULT FALSE | Traffic sign recognition |

---

## Assessment System

### assessments_vehicleassessment
**Main vehicle assessment record**

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | AutoField | PRIMARY KEY | Auto-incrementing primary key |
| assessment_id | CharField(50) | UNIQUE, NOT NULL | Assessment identifier |
| assessment_type | CharField(20) | NOT NULL | Assessment type |
| status | CharField(20) | DEFAULT 'pending' | Assessment status |
| user_id | ForeignKey | NOT NULL | Reference to auth_user |
| vehicle_id | ForeignKey | NOT NULL | Reference to vehicles_vehicle |
| organization_id | ForeignKey | NULL | Reference to organizations_organization |
| assessment_date | DateTimeField | AUTO_NOW_ADD | Assessment date |
| completed_date | DateTimeField | NULL | Completion date |
| assessor_name | CharField(100) | NOT NULL | Assessor name |
| assessor_certification | CharField(100) | NULL | Assessor certification |
| incident_location | CharField(255) | NULL | Incident location |
| incident_date | DateTimeField | NULL | Incident date |
| weather_conditions | CharField(100) | NULL | Weather conditions |
| overall_severity | CharField(20) | NOT NULL | Overall severity |
| uk_write_off_category | CharField(20) | NULL | UK write-off category |
| south_africa_70_percent_rule | BooleanField | DEFAULT FALSE | 70% rule flag |
| estimated_repair_cost | DecimalField(10,2) | NULL | Estimated repair cost |
| vehicle_market_value | DecimalField(10,2) | NULL | Vehicle market value |
| salvage_value | DecimalField(10,2) | NULL | Salvage value |
| overall_notes | TextField | NULL | Overall notes |
| recommendations | TextField | NULL | Recommendations |
| assigned_agent_id | ForeignKey | NULL | Assigned insurance agent |
| agent_status | CharField(20) | DEFAULT 'pending_review' | Agent review status |
| agent_notes | TextField | NULL | Agent notes |
| review_deadline | DateTimeField | NULL | Review deadline |
| uses_parts_based_quotes | BooleanField | DEFAULT TRUE | Parts-based quotes flag |
| parts_identification_complete | BooleanField | DEFAULT FALSE | Parts ID complete |
| quote_collection_status | CharField(20) | DEFAULT 'not_started' | Quote collection status |
| created_at | DateTimeField | AUTO_NOW_ADD | Record creation timestamp |
| updated_at | DateTimeField | AUTO_NOW | Record update timestamp |

**Assessment Types:**
- crash, pre_purchase, periodic, insurance_claim, total_loss

**Status Options:**
- pending, in_progress, under_review, completed, disputed, cancelled

**Severity Levels:**
- cosmetic, minor, moderate, major, total_loss

### assessments_exteriorbodydamage
**Exterior body damage assessment (38 points)**

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| assessment_id | OneToOneField | PRIMARY KEY | Reference to assessments_vehicleassessment |

**Front End (10 points):**
- front_bumper, hood, front_grille, headlight_housings, headlight_lenses
- front_fenders, front_quarter_panels, fog_light_housings, license_plate_bracket, front_spoiler_air_dam
- Each with corresponding _notes field

**Side Panels (10 points):**
- driver_side_door, passenger_side_door, rear_doors, door_frames, side_mirrors
- side_moldings_trim, rocker_panels, wheel_well_liners, side_windows, door_handles
- Each with corresponding _notes field

**Rear End (10 points):**
- rear_bumper, trunk_hatch, rear_quarter_panels, taillight_housings, taillight_lenses
- rear_window, rear_spoiler, exhaust_tips, rear_license_plate_area, backup_camera
- Each with corresponding _notes field

**Roof and Pillars (8 points):**
- roof_panel, a_pillars, b_pillars, c_pillars, d_pillars, roof_rails, sunroof_moonroof, antenna
- Each with corresponding _notes field

**Damage Severity Options:**
- none, light, moderate, severe, destroyed

### assessments_wheelsandtires
**Wheels and tires assessment (12 points)**

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| assessment_id | OneToOneField | PRIMARY KEY | Reference to assessments_vehicleassessment |

**Assessment Points:**
- front_left_tire, front_right_tire, rear_left_tire, rear_right_tire
- front_left_wheel, front_right_wheel, rear_left_wheel, rear_right_wheel
- spare_tire, wheel_lug_nuts, tire_pressure_sensors, center_caps
- Each with corresponding _notes field

### assessments_interiordamage
**Interior damage assessment (19 points)**

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| assessment_id | OneToOneField | PRIMARY KEY | Reference to assessments_vehicleassessment |

**Seating and Upholstery (7 points):**
- driver_seat, passenger_seat, rear_seats, seat_belts, headrests, armrests, floor_mats

**Dashboard and Controls (8 points):**
- dashboard, steering_wheel, instrument_cluster, center_console
- climate_controls, radio_infotainment, glove_compartment, door_panels

**Glass and Visibility (4 points):**
- windshield, side_windows_interior, interior_mirrors, visors

### assessments_mechanicalsystems
**Mechanical systems assessment (20 points)**

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| assessment_id | OneToOneField | PRIMARY KEY | Reference to assessments_vehicleassessment |

**Engine Bay (8 points):**
- engine_block, radiator, battery, air_filter_housing
- belts_and_hoses, fluid_reservoirs, wiring_harnesses, engine_mounts

**Suspension and Steering (7 points):**
- shock_absorbers, struts, springs, control_arms, tie_rods, steering_rack, power_steering_pump

**Drivetrain (5 points):**
- transmission, differential, cv_joints, drive_shafts, clutch_system

**Condition Options:**
- excellent, good, fair, poor, failed

### assessments_electricalsystems
**Electrical systems assessment**

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| assessment_id | OneToOneField | PRIMARY KEY | Reference to assessments_vehicleassessment |

**Assessment Points:**
- battery_condition, alternator_function, starter_motor, fuse_box
- wiring_harness, lighting_systems, electronic_modules, charging_ports

### assessments_safetysystems
**Safety systems assessment**

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| assessment_id | OneToOneField | PRIMARY KEY | Reference to assessments_vehicleassessment |

**Assessment Points:**
- airbag_system, seat_belt_pretensioners, abs_system, stability_control
- parking_sensors, backup_camera, collision_avoidance, lane_departure

### assessments_framestructural
**Frame and structural assessment**

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| assessment_id | OneToOneField | PRIMARY KEY | Reference to assessments_vehicleassessment |

**Assessment Points:**
- frame_rails, unibody_structure, crumple_zones, door_frames
- roof_structure, floor_pan, firewall, structural_welds

### assessments_fluidsystems
**Fluid systems assessment**

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| assessment_id | OneToOneField | PRIMARY KEY | Reference to assessments_vehicleassessment |

**Assessment Points:**
- engine_oil, coolant_system, brake_fluid, transmission_fluid
- power_steering_fluid, windshield_washer, fuel_system

---

## Insurance Management

### insurance_app_insurancepolicy
**Insurance policy information**

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | AutoField | PRIMARY KEY | Auto-incrementing primary key |
| policy_number | CharField(20) | UNIQUE, NOT NULL | Policy number |
| policy_holder_id | ForeignKey | NOT NULL | Reference to auth_user |
| organization_id | ForeignKey | NULL | Reference to organizations_organization |
| start_date | DateField | NOT NULL | Policy start date |
| end_date | DateField | NOT NULL | Policy end date |
| premium_amount | DecimalField(10,2) | NOT NULL | Premium amount |
| status | CharField(20) | DEFAULT 'active' | Policy status |
| created_at | DateTimeField | AUTO_NOW_ADD | Record creation timestamp |
| updated_at | DateTimeField | AUTO_NOW | Record update timestamp |

**Status Options:**
- active, suspended, cancelled

### insurance_app_vehicle
**Insurance vehicle records**

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | AutoField | PRIMARY KEY | Auto-incrementing primary key |
| policy_id | ForeignKey | NOT NULL | Reference to insurance_app_insurancepolicy |
| vehicle_id | ForeignKey | NOT NULL | Reference to vehicles_vehicle |
| purchase_date | DateField | NOT NULL | Purchase date |
| current_condition | CharField(20) | DEFAULT 'good' | Current condition |
| vehicle_health_index | FloatField | DEFAULT 100.0 | Health index (0-100) |
| risk_score | FloatField | DEFAULT 1.0 | Risk score (0-10) |
| last_inspection_date | DateField | NULL | Last inspection date |
| created_at | DateTimeField | AUTO_NOW_ADD | Record creation timestamp |
| updated_at | DateTimeField | AUTO_NOW | Record update timestamp |

### insurance_app_maintenanceschedule
**Insurance maintenance scheduling**

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | AutoField | PRIMARY KEY | Auto-incrementing primary key |
| vehicle_id | ForeignKey | NOT NULL | Reference to insurance_app_vehicle |
| maintenance_type | CharField(30) | NOT NULL | Maintenance type |
| priority_level | CharField(10) | DEFAULT 'medium' | Priority level |
| scheduled_date | DateField | NOT NULL | Scheduled date |
| due_mileage | PositiveIntegerField | NULL | Due mileage |
| description | TextField | NULL | Description |
| is_completed | BooleanField | DEFAULT FALSE | Completion status |
| completed_date | DateField | NULL | Completion date |
| cost | DecimalField(10,2) | NULL | Cost |
| service_provider | CharField(100) | NULL | Service provider |
| scheduled_maintenance_id | ForeignKey | NULL | Link to maintenance app |
| created_at | DateTimeField | AUTO_NOW_ADD | Record creation timestamp |
| updated_at | DateTimeField | AUTO_NOW | Record update timestamp |

### insurance_app_maintenancecompliance
**Maintenance compliance tracking**

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| vehicle_id | OneToOneField | PRIMARY KEY | Reference to insurance_app_vehicle |
| overall_compliance_rate | FloatField | DEFAULT 100.0 | Overall compliance rate |
| critical_maintenance_compliance | FloatField | DEFAULT 100.0 | Critical maintenance compliance |
| overdue_count | IntegerField | DEFAULT 0 | Overdue count |
| completed_on_time_count | IntegerField | DEFAULT 0 | On-time completion count |
| total_scheduled_count | IntegerField | DEFAULT 0 | Total scheduled count |
| last_calculated | DateTimeField | AUTO_NOW | Last calculation timestamp |

### insurance_app_accident
**Accident records**

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | AutoField | PRIMARY KEY | Auto-incrementing primary key |
| vehicle_id | ForeignKey | NOT NULL | Reference to insurance_app_vehicle |
| accident_date | DateTimeField | NOT NULL | Accident date/time |
| severity | CharField(20) | NOT NULL | Accident severity |
| claim_amount | DecimalField(12,2) | NOT NULL | Claim amount |
| description | TextField | NOT NULL | Accident description |
| maintenance_related | BooleanField | DEFAULT FALSE | Maintenance related flag |
| related_maintenance_type | CharField(20) | NULL | Related maintenance type |
| days_since_last_maintenance | IntegerField | NULL | Days since last maintenance |
| fault_determination | CharField(100) | NULL | Fault determination |
| location | CharField(200) | NOT NULL | Accident location |
| weather_conditions | CharField(50) | NULL | Weather conditions |
| vehicle_history_id | OneToOneField | NULL | Link to vehicles_vehiclehistory |
| created_at | DateTimeField | AUTO_NOW_ADD | Record creation timestamp |

### insurance_app_vehicleconditionscore
**Vehicle condition scoring**

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | AutoField | PRIMARY KEY | Auto-incrementing primary key |
| vehicle_id | ForeignKey | NOT NULL | Reference to insurance_app_vehicle |
| assessment_date | DateField | NOT NULL | Assessment date |
| engine_score | FloatField | NOT NULL | Engine score (0-100) |
| transmission_score | FloatField | NOT NULL | Transmission score (0-100) |
| brake_score | FloatField | NOT NULL | Brake score (0-100) |
| tire_score | FloatField | NOT NULL | Tire score (0-100) |
| suspension_score | FloatField | NOT NULL | Suspension score (0-100) |
| electrical_score | FloatField | NOT NULL | Electrical score (0-100) |
| overall_score | FloatField | NOT NULL | Overall score (0-100) |
| assessment_type | CharField(20) | NOT NULL | Assessment type |
| notes | TextField | NULL | Assessment notes |
| created_at | DateTimeField | AUTO_NOW_ADD | Record creation timestamp |

### insurance_app_riskalert
**Risk alert system**

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | UUIDField | PRIMARY KEY | UUID primary key |
| vehicle_id | ForeignKey | NOT NULL | Reference to insurance_app_vehicle |
| alert_type | CharField(30) | NOT NULL | Alert type |
| severity | CharField(10) | NOT NULL | Alert severity |
| title | CharField(200) | NOT NULL | Alert title |
| description | TextField | NOT NULL | Alert description |
| risk_score_impact | FloatField | NOT NULL | Risk score impact |
| is_resolved | BooleanField | DEFAULT FALSE | Resolution status |
| resolved_date | DateTimeField | NULL | Resolution date |
| resolution_notes | TextField | NULL | Resolution notes |
| created_at | DateTimeField | AUTO_NOW_ADD | Record creation timestamp |

### insurance_app_riskassessmentmetrics
**Risk assessment metrics**

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | AutoField | PRIMARY KEY | Auto-incrementing primary key |
| policy_id | ForeignKey | NOT NULL | Reference to insurance_app_insurancepolicy |
| calculation_date | DateField | AUTO_NOW_ADD | Calculation date |
| portfolio_compliance_rate | FloatField | NOT NULL | Portfolio compliance rate |
| critical_maintenance_compliance | FloatField | NOT NULL | Critical maintenance compliance |
| avg_vehicle_health_index | FloatField | NOT NULL | Average health index |
| vehicles_excellent_condition | IntegerField | NOT NULL | Excellent condition count |
| vehicles_poor_condition | IntegerField | NOT NULL | Poor condition count |
| maintenance_related_accidents | IntegerField | NOT NULL | Maintenance-related accidents |
| total_accidents | IntegerField | NOT NULL | Total accidents |
| accident_correlation_rate | FloatField | NOT NULL | Accident correlation rate |
| high_risk_vehicles | IntegerField | NOT NULL | High-risk vehicles count |
| active_alerts | IntegerField | NOT NULL | Active alerts count |
| resolved_alerts_30d | IntegerField | NOT NULL | Resolved alerts (30 days) |

---

## Notifications & Alerts

### notifications_vehiclealert
**Vehicle alert system**

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | AutoField | PRIMARY KEY | Auto-incrementing primary key |
| vehicle_id | ForeignKey | NOT NULL | Reference to vehicles_vehicle |
| alert_type | CharField(50) | NOT NULL | Alert type |
| priority | CharField(10) | NOT NULL | Alert priority |
| title | CharField(200) | NOT NULL | Alert title |
| description | TextField | NOT NULL | Alert description |
| is_active | BooleanField | DEFAULT TRUE | Active status |
| created_at | DateTimeField | AUTO_NOW_ADD | Creation timestamp |
| resolved_at | DateTimeField | NULL | Resolution timestamp |

**Alert Types:**
- MAINTENANCE_OVERDUE, PART_REPLACEMENT, INSURANCE_EXPIRY, INSPECTION_DUE

**Priority Levels:**
- HIGH, MEDIUM, LOW

### notifications_vehiclecostanalytics
**Vehicle cost analytics**

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | AutoField | PRIMARY KEY | Auto-incrementing primary key |
| vehicle_id | ForeignKey | NOT NULL | Reference to vehicles_vehicle |
| month | DateField | NOT NULL | Analytics month |
| total_cost | DecimalField(10,2) | NOT NULL | Total cost |
| maintenance_cost | DecimalField(10,2) | NOT NULL | Maintenance cost |
| parts_cost | DecimalField(10,2) | NOT NULL | Parts cost |
| labor_cost | DecimalField(10,2) | NOT NULL | Labor cost |

**Constraints:**
- UNIQUE(vehicle_id, month)

---

## Onboarding System

### onboarding_pendingvehicleonboarding
**Pending vehicle onboarding requests**

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | AutoField | PRIMARY KEY | Auto-incrementing primary key |
| submitted_by_id | ForeignKey | NULL | User who submitted request |
| client_id | ForeignKey | NOT NULL | Client user |
| vehicle_data | JSONField | NOT NULL | Vehicle data |
| ownership_data | JSONField | NOT NULL | Ownership data |
| status_data | JSONField | NOT NULL | Status data |
| history_data | JSONField | NULL | History data |
| equipment_data | JSONField | NOT NULL | Equipment data |
| image_data | JSONField | NULL | Image data |
| status | CharField(10) | DEFAULT 'pending' | Approval status |
| submitted_at | DateTimeField | AUTO_NOW_ADD | Submission timestamp |
| reviewed_at | DateTimeField | NULL | Review timestamp |
| reviewed_by_id | ForeignKey | NULL | Reviewer user |

**Status Options:**
- pending, approved, rejected

### onboarding_customeronboarding
**Customer onboarding questionnaire**

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | AutoField | PRIMARY KEY | Auto-incrementing primary key |
| user_id | OneToOneField | NOT NULL | Reference to auth_user |
| customer_type | CharField(20) | NOT NULL | Customer type |
| preferred_communication | CharField(20) | DEFAULT 'email' | Communication preference |
| reminder_frequency | CharField(15) | DEFAULT 'monthly' | Reminder frequency |
| service_radius | CharField(5) | NOT NULL | Service radius |
| monthly_maintenance_budget | CharField(15) | NOT NULL | Monthly budget |
| mobile_service_interest | BooleanField | DEFAULT FALSE | Mobile service interest |
| emergency_service_interest | BooleanField | DEFAULT FALSE | Emergency service interest |
| maintenance_knowledge | CharField(15) | NOT NULL | Maintenance knowledge level |
| current_mechanic | CharField(200) | NULL | Current mechanic |
| maintenance_tracking_method | CharField(200) | NULL | Tracking method |
| biggest_maintenance_challenge | TextField | NULL | Biggest challenge |
| primary_goal | CharField(25) | NOT NULL | Primary goal |
| service_priority | CharField(15) | NOT NULL | Service priority |
| preferred_payment_model | CharField(20) | NOT NULL | Payment model preference |
| parts_preference | CharField(20) | NOT NULL | Parts preference |
| auto_insurance_provider | CharField(100) | NULL | Insurance provider |
| vehicle_under_warranty | BooleanField | DEFAULT FALSE | Warranty status |
| extended_warranty_interest | CharField(20) | NOT NULL | Extended warranty interest |
| how_heard_about_service | CharField(20) | NOT NULL | Referral source |
| potential_referrals | BooleanField | DEFAULT FALSE | Potential referrals |
| interested_in_referral_rewards | BooleanField | DEFAULT FALSE | Referral rewards interest |
| status | CharField(15) | DEFAULT 'in_progress' | Onboarding status |
| completed_date | DateTimeField | NULL | Completion date |
| created_at | DateTimeField | AUTO_NOW_ADD | Creation timestamp |
| updated_at | DateTimeField | AUTO_NOW | Update timestamp |

### onboarding_vehicleonboarding
**Vehicle-specific onboarding**

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | AutoField | PRIMARY KEY | Auto-incrementing primary key |
| customer_onboarding_id | OneToOneField | NOT NULL | Reference to onboarding_customeronboarding |
| vin_number | CharField(17) | NOT NULL | Vehicle VIN |
| make | CharField(50) | NULL | Vehicle make |
| model | CharField(50) | NULL | Vehicle model |
| year | IntegerField | NULL | Model year |
| primary_usage | CharField(20) | NOT NULL | Primary usage |
| current_odometer | PositiveIntegerField | NOT NULL | Current odometer |
| estimated_annual_mileage | CharField(10) | NOT NULL | Annual mileage estimate |
| typical_driving_conditions | CharField(15) | NOT NULL | Driving conditions |
| current_condition | CharField(10) | NOT NULL | Current condition |
| last_oil_change | DateField | NULL | Last oil change |
| last_major_service | DateField | NULL | Last major service |
| current_problems | TextField | NULL | Current problems |
| under_warranty | BooleanField | DEFAULT FALSE | Warranty status |
| warranty_expires | DateField | NULL | Warranty expiration |
| maintenance_preference | CharField(20) | NOT NULL | Maintenance preference |
| vehicle_nickname | CharField(50) | NULL | Vehicle nickname |
| added_at | DateTimeField | AUTO_NOW_ADD | Addition timestamp |
| updated_at | DateTimeField | AUTO_NOW | Update timestamp |

**Constraints:**
- UNIQUE(customer_onboarding_id, vin_number)

---

## Relationships Overview

### Primary Relationships

**Vehicle-Centric Relationships:**
- `vehicles_vehicle` → One-to-Many with `vehicles_vehicleownership`
- `vehicles_vehicle` → One-to-One with `vehicles_vehiclestatus`
- `vehicles_vehicle` → One-to-Many with `vehicles_vehiclehistory`
- `vehicles_vehicle` → One-to-Many with `vehicles_vehicleimage`
- `vehicles_vehicle` → One-to-One with `vehicles_vehiclevaluation`

**Equipment Relationships:**
- `vehicles_vehicle` → One-to-One with all `vehicle_equip_*` tables

**Maintenance Relationships:**
- `vehicles_vehicle` → One-to-Many with `maintenance_assignedvehicleplan`
- `vehicles_vehicle` → One-to-Many with `maintenance_history_maintenancerecord`
- `vehicles_vehicle` → One-to-Many with `maintenance_history_inspection`

**Assessment Relationships:**
- `vehicles_vehicle` → One-to-Many with `assessments_vehicleassessment`
- `assessments_vehicleassessment` → One-to-One with all assessment detail tables

**Organization Relationships:**
- `organizations_organization` → One-to-Many with `organizations_organizationuser`
- `organizations_organization` → One-to-Many with `organizations_organizationvehicle`
- `organizations_organization` → One-to-One with `organizations_insuranceorganization`

**User Relationships:**
- `auth_user` → One-to-One with `users_profile`
- `auth_user` → One-to-Many with `users_userrole`
- `auth_user` → One-to-Many with `users_dataconsent`

### Foreign Key Constraints

**Cascade Deletions:**
- Vehicle deletion cascades to all related records
- User deletion cascades to profiles and roles
- Organization deletion cascades to memberships

**Set NULL on Deletion:**
- Technician deletions set technician_id to NULL
- Reviewer deletions preserve records but remove reviewer reference

### Indexes

**Performance Indexes:**
- VIN numbers (unique)
- Assessment IDs (unique)
- Date fields for time-based queries
- Status fields for filtering
- Foreign key relationships

**Composite Indexes:**
- (vehicle_id, date) for maintenance records
- (organization_id, user_id) for memberships
- (assessment_id, status) for workflow queries

---

## Data Integrity Rules

### Validation Rules
1. **VIN Format**: 17-character alphanumeric validation
2. **Date Ranges**: End dates must be after start dates
3. **Numeric Ranges**: Scores constrained to 0-100, risk scores 0-10
4. **Status Transitions**: Workflow status changes follow business rules

### Business Rules
1. **Vehicle Ownership**: Only one current owner per vehicle
2. **Assessment Workflow**: Status progression follows defined paths
3. **Maintenance Scheduling**: Due dates calculated from intervals
4. **Insurance Compliance**: Risk scores trigger automatic actions

### Audit Trail
- All major entities include created_at/updated_at timestamps
- Assessment history tracks all changes
- Version control for critical assessment data
- User activity logging for compliance

---

*This schema supports a comprehensive vehicle management system with maintenance tracking, insurance assessments, detailed inspections, and organizational workflows.*