CREATE TABLE IF NOT EXISTS public.blog
(
    id integer NOT NULL DEFAULT nextval('blog_id_seq'::regclass),
    link character varying(150) COLLATE pg_catalog."default",
    CONSTRAINT blog_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.blog_translate
(
    id integer NOT NULL DEFAULT nextval('blog_translate_id_seq'::regclass),
    fk_blog integer NOT NULL,
    language character varying(5) COLLATE pg_catalog."default" NOT NULL,
    name character varying(100) COLLATE pg_catalog."default",
    description character varying(150) COLLATE pg_catalog."default",
    categories character varying(100) COLLATE pg_catalog."default",
    CONSTRAINT blog_translate_pkey PRIMARY KEY (id),
    CONSTRAINT fk_blog FOREIGN KEY (fk_blog)
        REFERENCES public.blog (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
);

CREATE TABLE IF NOT EXISTS public.experience
(
    id integer NOT NULL DEFAULT nextval('experience_id_seq'::regclass),
    CONSTRAINT experience_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.experience_translate
(
    id integer NOT NULL DEFAULT nextval('experience_translate_id_seq'::regclass),
    fk_experience integer NOT NULL DEFAULT nextval('experience_translate_fk_experience_seq'::regclass),
    language character varying(5) COLLATE pg_catalog."default",
    company character varying(100) COLLATE pg_catalog."default",
    ocuppation character varying(150) COLLATE pg_catalog."default",
    period character varying(50) COLLATE pg_catalog."default",
    CONSTRAINT experience_translate_pkey PRIMARY KEY (id),
    CONSTRAINT fk_experience FOREIGN KEY (fk_experience)
        REFERENCES public.experience (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);

CREATE TABLE IF NOT EXISTS public.formation
(
    id integer NOT NULL DEFAULT nextval('formation_id_seq'::regclass),
    CONSTRAINT formation_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.formation_translate
(
    id integer NOT NULL DEFAULT nextval('formation_translate_id_seq'::regclass),
    fk_formation integer NOT NULL DEFAULT nextval('formation_translate_fk_formation_seq'::regclass),
    language character varying(5) COLLATE pg_catalog."default",
    institution character varying(100) COLLATE pg_catalog."default",
    formation character varying(100) COLLATE pg_catalog."default",
    period character varying(50) COLLATE pg_catalog."default",
    CONSTRAINT formation_translate_pkey PRIMARY KEY (id),
    CONSTRAINT fk_project FOREIGN KEY (fk_formation)
        REFERENCES public.formation (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);

CREATE TABLE IF NOT EXISTS public.general
(
    id integer NOT NULL DEFAULT nextval('general_id_seq'::regclass),
    name character varying(50) COLLATE pg_catalog."default",
    full_name character varying(100) COLLATE pg_catalog."default",
    email character varying(100) COLLATE pg_catalog."default",
    number_phone character varying(50) COLLATE pg_catalog."default",
    github_link character varying(100) COLLATE pg_catalog."default",
    linkedin_link character varying(100) COLLATE pg_catalog."default",
    CONSTRAINT general_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.general_translate
(
    id integer NOT NULL DEFAULT nextval('general_translate_id_seq'::regclass),
    fk_general integer NOT NULL DEFAULT nextval('general_translate_fk_general_seq'::regclass),
    language character varying(5) COLLATE pg_catalog."default",
    short_description character varying(100) COLLATE pg_catalog."default",
    about character varying(1000) COLLATE pg_catalog."default",
    CONSTRAINT general_translate_pkey PRIMARY KEY (id),
    CONSTRAINT fk_general FOREIGN KEY (fk_general)
        REFERENCES public.general (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);

CREATE TABLE IF NOT EXISTS public.project
(
    id integer NOT NULL DEFAULT nextval('project_id_seq'::regclass),
    link character varying(200) COLLATE pg_catalog."default",
    CONSTRAINT project_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.project_translate
(
    id integer NOT NULL DEFAULT nextval('project_translate_id_seq'::regclass),
    fk_project integer,
    language character varying(5) COLLATE pg_catalog."default",
    name character varying(100) COLLATE pg_catalog."default",
    description character varying(150) COLLATE pg_catalog."default",
    languages character varying(100) COLLATE pg_catalog."default",
    CONSTRAINT project_translate_pkey PRIMARY KEY (id),
    CONSTRAINT fk_project FOREIGN KEY (fk_project)
        REFERENCES public.project (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
);

CREATE TABLE IF NOT EXISTS public.skills
(
    id integer NOT NULL DEFAULT nextval('skills_id_seq'::regclass),
    name character varying(50) COLLATE pg_catalog."default",
    link_icon character varying(200) COLLATE pg_catalog."default",
    CONSTRAINT skills_pkey PRIMARY KEY (id)
);
