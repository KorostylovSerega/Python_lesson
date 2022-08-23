--
-- PostgreSQL database dump
--

-- Dumped from database version 12.12
-- Dumped by pg_dump version 12.12

-- Started on 2022-08-23 18:38:36

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 2824 (class 1262 OID 16511)
-- Name: hw11; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE hw11 WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'Russian_Ukraine.1251' LC_CTYPE = 'Russian_Ukraine.1251';


ALTER DATABASE hw11 OWNER TO postgres;

\connect hw11

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 203 (class 1259 OID 16514)
-- Name: dispatch; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.dispatch (
    id integer NOT NULL,
    client character varying(256),
    dec_number character varying(256),
    city character varying(256),
    deport integer
);


ALTER TABLE public.dispatch OWNER TO postgres;

--
-- TOC entry 202 (class 1259 OID 16512)
-- Name: dispatch_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.dispatch_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dispatch_id_seq OWNER TO postgres;

--
-- TOC entry 2825 (class 0 OID 0)
-- Dependencies: 202
-- Name: dispatch_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.dispatch_id_seq OWNED BY public.dispatch.id;


--
-- TOC entry 2688 (class 2604 OID 16517)
-- Name: dispatch id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dispatch ALTER COLUMN id SET DEFAULT nextval('public.dispatch_id_seq'::regclass);


--
-- TOC entry 2818 (class 0 OID 16514)
-- Dependencies: 203
-- Data for Name: dispatch; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.dispatch (id, client, dec_number, city, deport) VALUES (3, 'Juriy Stepanenko', '20450568745961', 'Kiev', 10);
INSERT INTO public.dispatch (id, client, dec_number, city, deport) VALUES (4, 'Julia Petkevich', '20450568768176', 'Krivoy Rog', 27);
INSERT INTO public.dispatch (id, client, dec_number, city, deport) VALUES (5, 'Oksana Gorban', '20450568769013', 'Brovary', 6);
INSERT INTO public.dispatch (id, client, dec_number, city, deport) VALUES (6, 'Alexandr Chernish', '20450568772561', 'Noviy Kaliniv', 1);
INSERT INTO public.dispatch (id, client, dec_number, city, deport) VALUES (7, 'Nagit Tomaev', '20450568780834', 'Odessa', 122);
INSERT INTO public.dispatch (id, client, dec_number, city, deport) VALUES (8, 'Anatoliy Gordieno', '20450568778796', 'Kiev', 215);
INSERT INTO public.dispatch (id, client, dec_number, city, deport) VALUES (1, 'Sergey_Savenkov', '20450568712797', 'Dnepr', 19);
INSERT INTO public.dispatch (id, client, dec_number, city, deport) VALUES (2, 'Vladimir Kovalchuk', '20450568714220', 'Dnepr', 14);
INSERT INTO public.dispatch (id, client, dec_number, city, deport) VALUES (11, 'Anatoliy Gordieno', '20488888555526', 'Kiev', 225);


--
-- TOC entry 2826 (class 0 OID 0)
-- Dependencies: 202
-- Name: dispatch_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.dispatch_id_seq', 11, true);


--
-- TOC entry 2690 (class 2606 OID 16522)
-- Name: dispatch dispatch_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dispatch
    ADD CONSTRAINT dispatch_pkey PRIMARY KEY (id);


-- Completed on 2022-08-23 18:38:37

--
-- PostgreSQL database dump complete
--

