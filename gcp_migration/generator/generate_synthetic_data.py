#!/usr/bin/env python3
"""
generate_synthetic_data.py
Generates statistically representative synthetic data for 7 Medallion sources:
1. index_0001: zoloto585_crm (Retail/Pawnshop CRM)
2. index_0696: dozarplati_loans (Microfinance loans)
3. index_0800: duhirf_ecommerce (E-commerce store)
4. index_0801: skb_techno_clients (B2B/B2C company registry)
5. index_0020_movements: sirena_rail_tickets (Passenger rail tickets)
6. index_0500_gibdd_spb: gibdd_vehicle_registry (Traffic police vehicle registry)
7. index_0080: gaming_platform_profiles (Online digital footprint / IPs / Telegram)

Includes injected real-world anomalies (phone corruptions, placeholder dates, nulls)
and shared identity anchors to validate cross-source entity resolution.
"""

import argparse
import csv
import hashlib
import os
import random
from datetime import date, datetime, timedelta
from typing import Dict, List, Tuple

# Deterministic random seed
RANDOM_SEED = 42
random.seed(RANDOM_SEED)

FIRST_NAMES_M = ["Андрей", "Сергей", "Иван", "Александр", "Дмитрий", "Максим", "Михаил", "Виталий", "Олег", "Николай"]
LAST_NAMES_M = ["Стариков", "Вахрущев", "Бамбуров", "Гульчевский", "Иванов", "Петров", "Смирнов", "Кузнецов", "Попов", "Соколов"]
MIDDLE_NAMES_M = ["Владимирович", "Петрович", "Сергеевич", "Геннадьевич", "Иванович", "Александрович", "Дмитриевич", "Николаевич"]

FIRST_NAMES_F = ["Светлана", "Татьяна", "Елена", "Ольга", "Полина", "Анастасия", "Наталья", "Анна", "Мария", "Екатерина"]
LAST_NAMES_F = ["Сержантова", "Михалевская", "Крекотень", "Еманова", "Родионова", "Павлова", "Кондратьева", "Иванова", "Петрова", "Смирнова"]
MIDDLE_NAMES_F = ["Анатольевна", "Станиславовна", "Александровна", "Львовна", "Борисовна", "Викторовна", "Владимировна", "Сергеевна"]

CITIES = ["Санкт-Петербург", "Москва", "Екатеринбург", "Казань", "Ноябрьск", "Туймазы", "Йошкар-Ола", "Тамбов", "Иркутск", "Ставрополь"]
STREETS = ["Билимбаевская ул.", "Мичурина", "наб. Морская", "Ленина", "Советская", "Мира", "Победы", "Гагарина"]

CAR_MODELS = ["Lada Vesta", "Toyota Camry", "Hyundai Solaris", "Kia Rio", "Volkswagen Polo", "Skoda Octavia", "BMW 520", "Mercedes-Benz E200"]
CAR_COLORS = ["Белый", "Черный", "Серый", "Серебристый", "Синий", "Красный"]

COMPANIES = [
    ("ООО Магнит", "7701234567", "1027700123456"),
    ("ПАО Сбербанк", "7707083893", "1027700132195"),
    ("ООО СКБ Техно", "6671000000", "1056604000000"),
    ("ООО ДоЗарплаты", "7801999999", "1117847000000"),
    ("ООО Ритейл Групп", "7702555555", "1087746000000")
]

def hash_entity(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()

def make_random_phone(clean_digits: str = None, corrupt: bool = False) -> str:
    if corrupt:
        choice = random.random()
        if choice < 0.3:
            return "0"
        elif choice < 0.6:
            return "T476517MAILRU"
        elif choice < 0.8:
            return "     "
        else:
            return "77777777777"
    if clean_digits:
        return clean_digits
    prefix = random.choice(["7911", "7921", "7931", "7965", "7912", "7981", "7925", "7928", "7953"])
    suffix = f"{random.randint(1000000, 9999999)}"
    return f"{prefix}{suffix}"

def make_random_passport(clean_digits: str = None) -> str:
    if clean_digits:
        return clean_digits
    return f"{random.randint(10, 99)}{random.randint(10, 99)}{random.randint(100000, 999999)}"

def make_random_vin() -> str:
    chars = "ABCDEFGHJKLMNPRSTUVWXYZ0123456789"
    return "".join(random.choice(chars) for _ in range(17))

def make_random_plate() -> str:
    letters = "АВЕКМНОРСТУХ"
    reg = random.choice(["77", "78", "99", "178", "199", "16", "66"])
    return f"{random.choice(letters)}{random.randint(100, 999)}{random.choice(letters)}{random.choice(letters)}{reg}"

# Create 50 Core Seed Identities that will be linked across datasets
CORE_IDENTITIES = []
for i in range(100):
    is_male = (i % 2 == 0)
    if is_male:
        fio = f"{LAST_NAMES_M[i % len(LAST_NAMES_M)]} {FIRST_NAMES_M[i % len(FIRST_NAMES_M)]} {MIDDLE_NAMES_M[i % len(MIDDLE_NAMES_M)]}"
        first = FIRST_NAMES_M[i % len(FIRST_NAMES_M)]
        last = LAST_NAMES_M[i % len(LAST_NAMES_M)]
        middle = MIDDLE_NAMES_M[i % len(MIDDLE_NAMES_M)]
        sex = "M"
    else:
        fio = f"{LAST_NAMES_F[i % len(LAST_NAMES_F)]} {FIRST_NAMES_F[i % len(FIRST_NAMES_F)]} {MIDDLE_NAMES_F[i % len(MIDDLE_NAMES_F)]}"
        first = FIRST_NAMES_F[i % len(FIRST_NAMES_F)]
        last = LAST_NAMES_F[i % len(LAST_NAMES_F)]
        middle = MIDDLE_NAMES_F[i % len(MIDDLE_NAMES_F)]
        sex = "F"
    
    b_year = random.randint(1965, 2002)
    b_month = random.randint(1, 12)
    b_day = random.randint(1, 28)
    dob = f"{b_year:04d}-{b_month:02d}-{b_day:02d}"
    phone = make_random_phone()
    email = f"user_{i}_{first.lower()}@mail.ru"
    passport = make_random_passport()
    inn = f"77{random.randint(1000000000, 9999999999)}"
    snils = f"{random.randint(100, 999)}{random.randint(100, 999)}{random.randint(100, 999)}{random.randint(10, 99)}"
    city = CITIES[i % len(CITIES)]
    street = STREETS[i % len(STREETS)]
    house = str(random.randint(1, 120))
    car_model = CAR_MODELS[i % len(CAR_MODELS)]
    car_plate = make_random_plate()
    car_vin = make_random_vin()
    car_color = CAR_COLORS[i % len(CAR_COLORS)]
    car_year = random.randint(2010, 2023)
    ip_addr = f"185.220.{random.randint(10, 240)}.{random.randint(2, 250)}"
    tg_id = str(random.randint(100000000, 999999999))
    comp = COMPANIES[i % len(COMPANIES)]
    
    CORE_IDENTITIES.append({
        "fio": fio, "first": first, "last": last, "middle": middle, "sex": sex,
        "dob": dob, "phone": phone, "email": email, "passport": passport,
        "inn": inn, "snils": snils, "city": city, "street": street, "house": house,
        "car_model": car_model, "car_plate": car_plate, "car_vin": car_vin,
        "car_color": car_color, "car_year": car_year, "ip": ip_addr, "tg_id": tg_id,
        "company": comp[0], "company_inn": comp[1], "company_ogrn": comp[2]
    })

def generate_index_0001(out_dir: str, num_rows: int, ingest_date: str):
    """zoloto585_crm (Retail/Pawnshop CRM)"""
    file_path = os.path.join(out_dir, "index_0001_zoloto585_crm.csv")
    headers = [
        "source_id", "source_entity_id", "ingest_date", "ingest_timestamp", "file_name",
        "partner_id", "partner_number", "fio", "birth_date", "sex", "phone_number",
        "email", "postal_code", "city", "street", "house_number", "room_number",
        "passport_number", "passport_type", "passport_text", "passport_valid_from",
        "passport_valid_to", "lombard_rating", "date_operation"
    ]
    with open(file_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        for i in range(num_rows):
            cid = CORE_IDENTITIES[i % len(CORE_IDENTITIES)] if i < len(CORE_IDENTITIES) * 2 else None
            p_id = str(1000000 + i)
            p_num = f"0007{random.randint(100000, 999999)}"
            corrupt = (random.random() < 0.05)
            
            fio = cid["fio"] if cid else f"{random.choice(LAST_NAMES_M)} {random.choice(FIRST_NAMES_M)} {random.choice(MIDDLE_NAMES_M)}"
            if corrupt and random.random() < 0.5:
                fio = fio.lower()
            elif corrupt:
                fio = "   "
                
            dob = cid["dob"] if cid else f"{random.randint(1970, 2000):04d}-{random.randint(1,12):02d}-{random.randint(1,28):02d}"
            if corrupt:
                dob = "1900-01-01"
                
            sex = cid["sex"] if cid else random.choice(["M", "F", "U"])
            phone = make_random_phone(cid["phone"] if cid else None, corrupt=corrupt)
            email = cid["email"] if cid and random.random() > 0.4 else ""
            city = cid["city"] if cid else random.choice(CITIES)
            street = cid["street"] if cid else random.choice(STREETS)
            passport = cid["passport"] if cid and random.random() > 0.3 else ""
            
            eid = hash_entity(f"index_0001:{p_id}:{p_num}:{phone}")
            ts = f"{ingest_date} 08:{random.randint(10,59):02d}:00"
            
            writer.writerow([
                "index_0001", eid, ingest_date, ts, "zoloto585.ru.csv",
                p_id, p_num, fio, dob, sex, phone, email, "190000", city, street,
                str(random.randint(1, 50)), str(random.randint(1, 100)),
                passport, "Паспорт гражданина РФ", "ТП ОУФМС России",
                "2015-05-10", "9999-12-31", str(random.randint(0, 5)), ts
            ])

def generate_index_0696(out_dir: str, num_rows: int, ingest_date: str):
    """dozarplati_loans (Microfinance)"""
    file_path = os.path.join(out_dir, "index_0696_dozarplati_loans.csv")
    headers = [
        "source_id", "source_entity_id", "ingest_date", "ingest_timestamp", "file_name",
        "last_name", "first_name", "middle_name", "birth_date", "mobile_phone",
        "email", "registration_address", "organization_name", "job_title",
        "application_date", "loan_amount", "loan_status"
    ]
    with open(file_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        for i in range(num_rows):
            cid = CORE_IDENTITIES[i % len(CORE_IDENTITIES)] if i < len(CORE_IDENTITIES) * 2 else None
            last = cid["last"] if cid else random.choice(LAST_NAMES_M)
            first = cid["first"] if cid else random.choice(FIRST_NAMES_M)
            mid = cid["middle"] if cid else random.choice(MIDDLE_NAMES_M)
            dob = cid["dob"] if cid else "1985-06-15"
            phone = cid["phone"] if cid else make_random_phone()
            email = cid["email"] if cid and random.random() > 0.3 else ""
            comp = cid["company"] if cid else random.choice(COMPANIES)[0]
            addr = f"{cid['city']}, {cid['street']}, {cid['house']}" if cid else "г. Москва, ул. Ленина, д. 5"
            
            eid = hash_entity(f"index_0696:{last}:{first}:{phone}:{i}")
            ts = f"{ingest_date} 09:{random.randint(10,59):02d}:00"
            amount = str(random.randint(5, 50) * 1000)
            status = random.choice(["Одобрено", "Выдано", "Отклонено", "Закрыто"])
            
            writer.writerow([
                "index_0696", eid, ingest_date, ts, "dozarplati_loans.csv",
                last, first, mid, dob, phone, email, addr, comp,
                random.choice(["Менеджер", "Инженер", "Водитель", "Директор", "Бухгалтер"]),
                ts[:10], amount, status
            ])

def generate_index_0800(out_dir: str, num_rows: int, ingest_date: str):
    """duhirf_ecommerce (E-commerce store)"""
    file_path = os.path.join(out_dir, "index_0800_duhirf_ecommerce.csv")
    headers = [
        "source_id", "source_entity_id", "ingest_date", "ingest_timestamp", "file_name",
        "customer_id", "last_name", "first_name", "middle_name", "birthday",
        "phone_number", "personal_discount", "total_order_amount", "bonus_points"
    ]
    with open(file_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        for i in range(num_rows):
            cid = CORE_IDENTITIES[i % len(CORE_IDENTITIES)] if i < len(CORE_IDENTITIES) * 2 else None
            cust_id = str(200000 + i)
            last = cid["last"] if cid else random.choice(LAST_NAMES_F)
            first = cid["first"] if cid else random.choice(FIRST_NAMES_F)
            mid = cid["middle"] if cid else random.choice(MIDDLE_NAMES_F)
            dob = cid["dob"] if cid else "1992-04-12"
            phone = cid["phone"] if cid else make_random_phone()
            
            eid = hash_entity(f"index_0800:{cust_id}:{phone}")
            ts = f"{ingest_date} 10:{random.randint(10,59):02d}:00"
            
            writer.writerow([
                "index_0800", eid, ingest_date, ts, "duhirf_customers.csv",
                cust_id, last, first, mid, dob, phone,
                str(random.choice([0, 5, 10, 15])),
                str(random.randint(1500, 45000)),
                str(random.randint(0, 500))
            ])

def generate_index_0801(out_dir: str, num_rows: int, ingest_date: str):
    """skb_techno_clients (B2B/B2C Company & Client Registry)"""
    file_path = os.path.join(out_dir, "index_0801_skb_techno_clients.csv")
    headers = [
        "source_id", "source_entity_id", "ingest_date", "ingest_timestamp", "file_name",
        "inn", "ogrn", "company_name", "last_name", "first_name", "middle_name",
        "birth_date", "birth_place", "sex", "document_type", "document_serial",
        "document_number", "document_date", "document_issuer", "document_code",
        "snils", "inn_person", "address", "post_address", "phone", "email", "agent_title"
    ]
    with open(file_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        for i in range(num_rows):
            cid = CORE_IDENTITIES[i % len(CORE_IDENTITIES)] if i < len(CORE_IDENTITIES) * 2 else None
            last = cid["last"] if cid else random.choice(LAST_NAMES_M)
            first = cid["first"] if cid else random.choice(FIRST_NAMES_M)
            mid = cid["middle"] if cid else random.choice(MIDDLE_NAMES_M)
            dob = cid["dob"] if cid else "1980-01-20"
            phone = cid["phone"] if cid else make_random_phone()
            email = cid["email"] if cid else f"info_{i}@company.ru"
            inn_p = cid["inn"] if cid else f"77{random.randint(1000000000, 9999999999)}"
            snils = cid["snils"] if cid else f"{random.randint(10000000000, 99999999999)}"
            comp = cid["company"] if cid else "ООО Технологии"
            comp_inn = cid["company_inn"] if cid else "7701999999"
            comp_ogrn = cid["company_ogrn"] if cid else "1027700000000"
            
            eid = hash_entity(f"index_0801:{comp_inn}:{inn_p}:{phone}")
            ts = f"{ingest_date} 11:{random.randint(10,59):02d}:00"
            
            writer.writerow([
                "index_0801", eid, ingest_date, ts, "skb_clients.csv",
                comp_inn, comp_ogrn, comp, last, first, mid,
                dob, cid["city"] if cid else "Москва", "M", "Паспорт РФ",
                cid["passport"][:4] if cid else "4012",
                cid["passport"][4:] if cid else "686811",
                "2018-03-15", "ГУ МВД России", "770-001",
                snils, inn_p, f"{cid['city']}, {cid['street']}" if cid else "Москва",
                "101000, Москва", phone, email, "Генеральный директор"
            ])

def generate_index_0020(out_dir: str, num_rows: int, ingest_date: str):
    """sirena_rail_tickets (Passenger Rail Movements - index_0020)"""
    file_path = os.path.join(out_dir, "index_0020_sirena.csv")
    headers = [
        "source_id", "source_entity_id", "ingest_date", "ingest_timestamp", "file_name",
        "ticket_number", "passenger_doc", "passenger_name", "seat_tier", "seat",
        "ticket_date", "citizenship", "phone", "birth_date", "departure_date",
        "arrival_date", "port_from", "port_to", "train", "coach_class", "coach_number", "coach_type"
    ]
    with open(file_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        for i in range(num_rows):
            cid = CORE_IDENTITIES[i % len(CORE_IDENTITIES)] if i < len(CORE_IDENTITIES) * 2 else None
            tkt = f"TK{random.randint(10000000, 99999999)}"
            name = cid["fio"] if cid else f"{random.choice(LAST_NAMES_M)} {random.choice(FIRST_NAMES_M)}"
            doc = cid["passport"] if cid else make_random_passport()
            dob = cid["dob"] if cid else "1988-07-22"
            phone = cid["phone"] if cid else make_random_phone()
            dep = ingest_date
            
            eid = hash_entity(f"index_0020:{tkt}:{doc}:{dep}")
            ts = f"{ingest_date} 12:{random.randint(10,59):02d}:00"
            
            writer.writerow([
                "index_0020", eid, ingest_date, ts, "sirena_tickets.csv",
                tkt, doc, name, "2", str(random.randint(1, 36)),
                ingest_date, "RUS", phone, dob, dep, dep,
                random.choice(["МОСКВА", "САНКТ-ПЕТЕРБУРГ", "ЕКАТЕРИНБУРГ", "КАЗАНЬ"]),
                random.choice(["САНКТ-ПЕТЕРБУРГ", "МОСКВА", "НИЖНИЙ НОВГОРОД", "СОЧИ"]),
                f"00{random.randint(1, 9)}А", "КУПЕ", str(random.randint(1, 14)), "К"
            ])

def generate_index_0500(out_dir: str, num_rows: int, ingest_date: str):
    """gibdd_vehicle_registry (Auto Police Registrations - index_0500)"""
    file_path = os.path.join(out_dir, "index_0500_vehicles.csv")
    headers = [
        "source_id", "source_entity_id", "ingest_date", "ingest_timestamp", "file_name",
        "fio", "birth_date", "phone", "passport", "license_plate",
        "vin", "model", "manufacture_year", "color", "company_name",
        "company_inn", "company_ogrn"
    ]
    with open(file_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        for i in range(num_rows):
            cid = CORE_IDENTITIES[i % len(CORE_IDENTITIES)] if i < len(CORE_IDENTITIES) * 2 else None
            fio = cid["fio"] if cid else f"{random.choice(LAST_NAMES_M)} {random.choice(FIRST_NAMES_M)}"
            dob = cid["dob"] if cid else "1983-04-19"
            phone = cid["phone"] if cid else make_random_phone()
            passport = cid["passport"] if cid else make_random_passport()
            plate = cid["car_plate"] if cid else make_random_plate()
            vin = cid["car_vin"] if cid else make_random_vin()
            model = cid["car_model"] if cid else random.choice(CAR_MODELS)
            year = str(cid["car_year"] if cid else random.randint(2010, 2022))
            color = cid["car_color"] if cid else random.choice(CAR_COLORS)
            
            eid = hash_entity(f"index_0500:{plate}:{vin}:{phone}")
            ts = f"{ingest_date} 13:{random.randint(10,59):02d}:00"
            
            writer.writerow([
                "index_0500", eid, ingest_date, ts, "gibdd_spb.csv",
                fio, dob, phone, passport, plate, vin, model, year, color,
                "", "", ""
            ])

def generate_index_0080(out_dir: str, num_rows: int, ingest_date: str):
    """gaming_platform_profiles (Online digital footprint / IPs / Telegram)"""
    file_path = os.path.join(out_dir, "index_0080_gaming_profiles.csv")
    headers = [
        "source_id", "source_entity_id", "ingest_date", "ingest_timestamp", "file_name",
        "account_id", "email", "phone", "user_name", "country",
        "birthday", "passport", "address", "passport_by", "last_ip",
        "last_ip_country", "telegram_id", "timezone", "registration_time"
    ]
    with open(file_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        for i in range(num_rows):
            cid = CORE_IDENTITIES[i % len(CORE_IDENTITIES)] if i < len(CORE_IDENTITIES) * 2 else None
            acc_id = str(500000 + i)
            email = cid["email"] if cid else f"gamer_{i}@mail.ru"
            phone = cid["phone"] if cid else make_random_phone()
            user = cid["fio"] if cid else f"Player_{i}"
            dob = cid["dob"] if cid else "1995-11-03"
            passport = cid["passport"] if cid and random.random() > 0.4 else ""
            ip = cid["ip"] if cid else f"185.220.{random.randint(10, 240)}.{random.randint(2, 250)}"
            tg = cid["tg_id"] if cid else str(random.randint(100000000, 999999999))
            
            eid = hash_entity(f"index_0080:{acc_id}:{ip}:{tg}")
            ts = f"{ingest_date} 14:{random.randint(10,59):02d}:00"
            
            writer.writerow([
                "index_0080", eid, ingest_date, ts, "gaming_users.csv",
                acc_id, email, phone, user, "RU", dob, passport,
                cid["city"] if cid else "Москва", "МВД", ip, "RU", tg,
                "Europe/Moscow", ts
            ])

def generate_index_0042(out_dir: str, num_rows: int, ingest_date: str):
    """delivery_orders (Food & Courier delivery checkout orders)"""
    file_path = os.path.join(out_dir, "index_0042_delivery_orders.csv")
    headers = [
        "source_id", "source_entity_id", "customer_name", "phone", "email",
        "delivery_city", "delivery_address", "order_amount", "order_date", "device_ip"
    ]
    with open(file_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        for i in range(num_rows):
            cid = CORE_IDENTITIES[i % len(CORE_IDENTITIES)] if i < len(CORE_IDENTITIES) * 2 else None
            ord_id = f"ORD_0042_{i+1:06d}"
            name = cid["fio"] if cid else f"Customer_{i}"
            phone = cid["phone"] if cid else make_random_phone()
            email = cid["email"] if cid else f"delivery_client_{i}@mail.ru"
            city = cid["city"] if cid else random.choice(CITIES)
            address = f"{random.choice(STREETS)}, д. {random.randint(1, 150)}, кв. {random.randint(1, 200)}"
            amount = f"{random.randint(500, 7500):.2f}"
            ip = cid["ip"] if cid else f"194.28.{random.randint(10, 240)}.{random.randint(2, 250)}"
            writer.writerow([
                "index_0042", ord_id, name, phone, email,
                city, address, amount, ingest_date, ip
            ])

def main():
    parser = argparse.ArgumentParser(description="Generate Medallion synthetic datasets.")
    parser.add_argument("--mode", choices=["sample", "full"], default="sample",
                        help="Data generation mode: 'sample' (~1,000 rows/table, ~5MB) or 'full' (~50,000 rows/table, ~100MB+)")
    parser.add_argument("--out-dir", default="data/synthetic", help="Output directory")
    parser.add_argument("--date", default=date.today().isoformat(), help="Ingestion partition date (YYYY-MM-DD)")
    args = parser.parse_args()

    target_dir = os.path.join(args.out_dir, args.mode)
    os.makedirs(target_dir, exist_ok=True)

    rows_per_source = 1500 if args.mode == "sample" else 45000
    print(f"Generating synthetic data in mode: {args.mode.upper()}")
    print(f"Target directory: {target_dir}")
    print(f"Partition date:   {args.date}")
    print(f"Rows per source:  {rows_per_source:,}")

    generate_index_0001(target_dir, rows_per_source, args.date)
    generate_index_0696(target_dir, rows_per_source, args.date)
    generate_index_0800(target_dir, rows_per_source, args.date)
    generate_index_0801(target_dir, rows_per_source, args.date)
    generate_index_0020(target_dir, rows_per_source, args.date)
    generate_index_0500(target_dir, rows_per_source, args.date)
    generate_index_0080(target_dir, rows_per_source, args.date)
    generate_index_0042(target_dir, rows_per_source, args.date)

    total_size = sum(os.path.getsize(os.path.join(target_dir, f)) for f in os.listdir(target_dir) if f.endswith(".csv"))
    print(f"\nSuccessfully generated 8 source CSV files. Total size: {total_size / (1024 * 1024):.2f} MB")

if __name__ == "__main__":
    main()
