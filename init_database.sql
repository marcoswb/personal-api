CREATE TABLE IF NOT EXISTS public.blog
(
    id integer NOT NULL DEFAULT nextval('blog_id_seq'::regclass),
    name character varying(50)[] COLLATE pg_catalog."default",
    description character varying(120)[] COLLATE pg_catalog."default",
    link character varying(120)[] COLLATE pg_catalog."default",
    categories character varying(50)[] COLLATE pg_catalog."default"
);

CREATE TABLE IF NOT EXISTS public.experience
(
    id integer NOT NULL DEFAULT nextval('experience_id_seq'::regclass),
    company character varying(30)[] COLLATE pg_catalog."default",
    ocuppation character varying(30)[] COLLATE pg_catalog."default",
    period character varying(30)[] COLLATE pg_catalog."default"
);

CREATE TABLE IF NOT EXISTS public.formation
(
    id integer NOT NULL DEFAULT nextval('formation_id_seq'::regclass),
    institution character varying(60)[] COLLATE pg_catalog."default",
    formation character varying(60)[] COLLATE pg_catalog."default",
    period character varying(50)[] COLLATE pg_catalog."default"
);

CREATE TABLE IF NOT EXISTS public.general
(
    id integer NOT NULL DEFAULT nextval('general_id_seq'::regclass),
    name character varying(20) COLLATE pg_catalog."default",
    full_name character varying(50) COLLATE pg_catalog."default",
    short_description character varying(50) COLLATE pg_catalog."default",
    about character varying(1000) COLLATE pg_catalog."default",
    email character varying(30) COLLATE pg_catalog."default",
    number_phone character varying(12) COLLATE pg_catalog."default",
    github_link character varying(50) COLLATE pg_catalog."default",
    linkedin_link character varying(50) COLLATE pg_catalog."default"
);

CREATE TABLE IF NOT EXISTS public.project
(
    id integer NOT NULL DEFAULT nextval('project_id_seq'::regclass),
    name character varying(30)[] COLLATE pg_catalog."default",
    description character varying(100)[] COLLATE pg_catalog."default",
    link character varying(60)[] COLLATE pg_catalog."default",
    languages character varying(50)[] COLLATE pg_catalog."default"
);

CREATE TABLE IF NOT EXISTS public.skills
(
    id integer NOT NULL DEFAULT nextval('skills_id_seq'::regclass),
    name character varying(20)[] COLLATE pg_catalog."default",
    link_icon character varying(100)[] COLLATE pg_catalog."default"
);