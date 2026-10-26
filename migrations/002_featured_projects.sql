ALTER TABLE public.project
    ADD COLUMN IF NOT EXISTS featured boolean NOT NULL DEFAULT false;

ALTER TABLE public.project
    ADD COLUMN IF NOT EXISTS featured_order integer;

ALTER TABLE public.project
    ADD COLUMN IF NOT EXISTS "order" integer;
