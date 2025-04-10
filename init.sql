CREATE DATABASE "task_tracker";
CREATE ROLE app WITH LOGIN PASSWORD 'b2jrpI8JqG5H71zmf8lT';

GRANT CONNECT ON DATABASE task_tracker TO app;

\connect task_tracker

GRANT USAGE ON SCHEMA public TO app;
GRANT ALL PRIVILEGES ON SCHEMA public TO app;
GRANT CREATE ON SCHEMA public TO app;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO app;
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO app;