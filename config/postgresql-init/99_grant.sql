-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
-- helpdesk
-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
REVOKE ALL PRIVILEGES ON ALL TABLES IN SCHEMA public FROM backend;
REVOKE ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public FROM backend;

GRANT ALL PRIVILEGES ON DATABASE helpdesk TO backend;