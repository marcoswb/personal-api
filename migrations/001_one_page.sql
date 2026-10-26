ALTER TABLE public.general_translate
    ADD COLUMN IF NOT EXISTS role_title character varying(120);

ALTER TABLE public.experience_translate
    ADD COLUMN IF NOT EXISTS highlights text;

ALTER TABLE public.skills
    ADD COLUMN IF NOT EXISTS category character varying(30);
