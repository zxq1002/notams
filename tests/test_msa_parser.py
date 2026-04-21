import pytest
from datetime import datetime
from service.fetch.MSA_NAV_SEARCH import preprocess_text, parse_coordinates, parse_msa_time, infer_year

def test_preprocess_text():
    text = "  {abc} %def% \n\r line1 \n line2  "
    expected = "line1 line2"
    assert preprocess_text(text) == expected

def test_parse_coordinates():
    # Format 1: DD-MM.mmN DDD-MM.mmE (space separated)
    text1 = "31-15.00N 121-30.00E"
    assert parse_coordinates(text1) == ["N311500E1213000"]
    
    # Format 2: DD-MM.mmN/DDD-MM.mmE (slash separated)
    text2 = "31-15.00N/121-30.00E"
    assert parse_coordinates(text2) == ["N311500E1213000"]
    
    # Format 3: DD-MM.mmNDDD-MM.mmE (no separator)
    text3 = "31-15.00N121-30.00E"
    assert parse_coordinates(text3) == ["N311500E1213000"]
    
    # Multiple coordinates
    text4 = "31-15.00N 121-30.00E, 32-20.50N 122-40.25E"
    result = parse_coordinates(text4)
    assert len(result) == 2
    assert "N311500E1213000" in result
    # 20.50 -> 20 min, 0.50 * 60 = 30 sec
    # 40.25 -> 40 min, 0.25 * 60 = 15 sec
    assert "N322030E1224015" in result

def test_infer_year():
    # If published in Dec, and NOTAM month is Dec -> same year
    pub_date = datetime(2023, 12, 1)
    assert infer_year(12, pub_date) == 2023
    
    # If published in Dec, and NOTAM month is Jan -> next year
    assert infer_year(1, pub_date) == 2024
    
    # If published in Jan, and NOTAM month is Dec -> same year (or logic error in code?)
    # Current implementation: if pub_date.month <= month: return pub_date.year else: pub_date.year + 1
    pub_date_jan = datetime(2024, 1, 1)
    assert infer_year(12, pub_date_jan) == 2024 # Correct, it's for future events
    assert infer_year(1, pub_date_jan) == 2024

def test_parse_msa_time_pattern1():
    # 模式1: 完整日期 YYYY年MM月DD日HHMM时至HHMM时
    time_str = "2024年05月20日0800时至1200时"
    pub_date = "2024-05-19"
    result = parse_msa_time(time_str, pub_date)
    # 08:00 BJT -> 00:00 UTC, 12:00 BJT -> 04:00 UTC
    assert "20 MAY 00:00 2024 UNTIL 20 MAY 04:00 2024" in result

def test_parse_msa_time_pattern2():
    # 模式2: 完整日期范围 YYYY年MM月DD日至YYYY年MM月DD日
    time_str = "2024年05月20日至2024年05月22日"
    pub_date = "2024-05-19"
    result = parse_msa_time(time_str, pub_date)
    # Start: 05-20 00:00 BJT -> 05-19 16:00 UTC
    # End: 05-22 23:59 BJT -> 05-22 15:59 UTC
    assert "19 MAY 16:00 2024 UNTIL 22 MAY 15:59 2024" in result

def test_parse_msa_time_pattern3():
    # 模式3: 完整日期 YYYY年MM月DD日至MM月DD日
    time_str = "2023年12月30日至01月02日"
    pub_date = "2023-12-25"
    result = parse_msa_time(time_str, pub_date)
    # Start: 2023-12-30 00:00 BJT -> 2023-12-29 16:00 UTC
    # End: 2024-01-02 23:59 BJT -> 2024-01-02 15:59 UTC
    assert "29 DEC 16:00 2023 UNTIL 02 JAN 15:59 2024" in result

def test_parse_msa_time_pattern4():
    # 模式4: MM月DD日HHMM时至DD日HHMM时 (跨天)
    time_str = "05月20日0800时至21日1200时"
    pub_date = "2024-05-19"
    result = parse_msa_time(time_str, pub_date)
    assert "20 MAY 00:00 2024 UNTIL 21 MAY 04:00 2024" in result

def test_parse_msa_time_pattern5():
    # 模式5: MM月DD日HHMM时至HHMM时 (同一天)
    time_str = "05月20日0800时至1200时"
    pub_date = "2024-05-19"
    result = parse_msa_time(time_str, pub_date)
    assert "20 MAY 00:00 2024 UNTIL 20 MAY 04:00 2024" in result

def test_parse_msa_time_pattern6():
    # 模式6: 自YYYY年MM月DD日HHMM时至HHMM时
    time_str = "自2024年05月20日0800时至1200时"
    pub_date = "2024-05-19"
    result = parse_msa_time(time_str, pub_date)
    assert "20 MAY 00:00 2024 UNTIL 20 MAY 04:00 2024" in result
