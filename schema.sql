drop table if exists hookups;
create table hookups (
    hooker text not null,
    hookee text not null,
    reason text not null,
    year int
);
