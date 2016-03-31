drop table if exists hookups;
create table hookups (
	id integer primary key autoincrement,
    hooker text not null,
    hookee text not null,
    reason text not null,
    year integer
);
