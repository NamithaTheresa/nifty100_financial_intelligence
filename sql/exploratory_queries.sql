-- ===========================================
-- Exploratory SQL Queries
-- ===========================================

-- 1. Total number of companies
SELECT COUNT(*) AS total_companies
FROM companies;

-- 2. Total records in Profit and Loss table
SELECT COUNT(*) AS total_profitandloss_records
FROM profitandloss;

-- 3. Total records in each table
SELECT 'companies' AS table_name, COUNT(*) AS total_rows FROM companies
UNION ALL
SELECT 'profitandloss', COUNT(*) FROM profitandloss
UNION ALL
SELECT 'balancesheet', COUNT(*) FROM balancesheet
UNION ALL
SELECT 'cashflow', COUNT(*) FROM cashflow
UNION ALL
SELECT 'analysis', COUNT(*) FROM analysis
UNION ALL
SELECT 'documents', COUNT(*) FROM documents
UNION ALL
SELECT 'prosandcons', COUNT(*) FROM prosandcons
UNION ALL
SELECT 'stock_prices', COUNT(*) FROM stock_prices
UNION ALL
SELECT 'financial_ratios', COUNT(*) FROM financial_ratios
UNION ALL
SELECT 'market_cap', COUNT(*) FROM market_cap
UNION ALL
SELECT 'peer_groups', COUNT(*) FROM peer_groups
UNION ALL
SELECT 'sectors', COUNT(*) FROM sectors;

-- 4. Check for NULL company IDs
SELECT COUNT(*) AS null_company_ids
FROM profitandloss
WHERE company_id IS NULL;

-- 5. Number of years available for each company
SELECT
    company_id,
    COUNT(year) AS total_years
FROM profitandloss
GROUP BY company_id
ORDER BY total_years DESC;

-- 6. Year coverage for each company
SELECT
    company_id,
    MIN(year) AS first_year,
    MAX(year) AS last_year
FROM profitandloss
GROUP BY company_id
ORDER BY company_id;

-- 7. Check duplicate Company-Year records
SELECT
    company_id,
    year,
    COUNT(*) AS duplicate_count
FROM financial_ratios
GROUP BY company_id, year
HAVING COUNT(*) > 1;

-- 8. Average Sales
SELECT
    AVG(sales) AS average_sales
FROM profitandloss;

-- 9. Top 10 companies by Market Capitalization
SELECT
    company_id,
    MAX(market_cap_crore) AS highest_market_cap
FROM market_cap
GROUP BY company_id
ORDER BY highest_market_cap DESC
LIMIT 10;

-- 10. Number of Stock Price Records per Company
SELECT
    company_id,
    COUNT(*) AS total_stock_records
FROM stock_prices
GROUP BY company_id
ORDER BY total_stock_records DESC;