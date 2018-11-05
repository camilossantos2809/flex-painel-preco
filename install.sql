create user painel;
alter user painel encrypted password '123456';
grant SELECT, references ON ALL tables in schema public TO painel;
alter default privileges in schema public grant select, references on tables to painel;
create schema if not exists painel authorization painel;
