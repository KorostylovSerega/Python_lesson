--
-- PostgreSQL database dump
--

-- Dumped from database version 12.12
-- Dumped by pg_dump version 12.12

-- Started on 2022-08-19 15:49:57

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
-- TOC entry 205 (class 1259 OID 16420)
-- Name: genre; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.genre (
    id integer NOT NULL,
    name character varying(255) NOT NULL
);


ALTER TABLE public.genre OWNER TO postgres;

--
-- TOC entry 204 (class 1259 OID 16418)
-- Name: genre_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.genre_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.genre_id_seq OWNER TO postgres;

--
-- TOC entry 2890 (class 0 OID 0)
-- Dependencies: 204
-- Name: genre_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.genre_id_seq OWNED BY public.genre.id;


--
-- TOC entry 203 (class 1259 OID 16412)
-- Name: movie; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.movie (
    id integer NOT NULL,
    title character varying(255) NOT NULL,
    year character(4)
);


ALTER TABLE public.movie OWNER TO postgres;

--
-- TOC entry 206 (class 1259 OID 16426)
-- Name: movie_genre; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.movie_genre (
    movie_id integer,
    genre_id integer
);


ALTER TABLE public.movie_genre OWNER TO postgres;

--
-- TOC entry 202 (class 1259 OID 16410)
-- Name: movie_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.movie_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.movie_id_seq OWNER TO postgres;

--
-- TOC entry 2891 (class 0 OID 0)
-- Dependencies: 202
-- Name: movie_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.movie_id_seq OWNED BY public.movie.id;


--
-- TOC entry 213 (class 1259 OID 16476)
-- Name: movie_staff; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.movie_staff (
    movie_id integer,
    staff_position_id integer
);


ALTER TABLE public.movie_staff OWNER TO postgres;

--
-- TOC entry 210 (class 1259 OID 16452)
-- Name: position; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."position" (
    id integer NOT NULL,
    name character varying(255) NOT NULL
);


ALTER TABLE public."position" OWNER TO postgres;

--
-- TOC entry 209 (class 1259 OID 16450)
-- Name: position_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.position_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.position_id_seq OWNER TO postgres;

--
-- TOC entry 2892 (class 0 OID 0)
-- Dependencies: 209
-- Name: position_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.position_id_seq OWNED BY public."position".id;


--
-- TOC entry 208 (class 1259 OID 16441)
-- Name: staff; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.staff (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    surname character varying(255) NOT NULL
);


ALTER TABLE public.staff OWNER TO postgres;

--
-- TOC entry 207 (class 1259 OID 16439)
-- Name: staff_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.staff_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.staff_id_seq OWNER TO postgres;

--
-- TOC entry 2893 (class 0 OID 0)
-- Dependencies: 207
-- Name: staff_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.staff_id_seq OWNED BY public.staff.id;


--
-- TOC entry 212 (class 1259 OID 16460)
-- Name: staff_position; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.staff_position (
    id integer NOT NULL,
    staff_id integer,
    position_id integer
);


ALTER TABLE public.staff_position OWNER TO postgres;

--
-- TOC entry 211 (class 1259 OID 16458)
-- Name: staff_position_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.staff_position_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.staff_position_id_seq OWNER TO postgres;

--
-- TOC entry 2894 (class 0 OID 0)
-- Dependencies: 211
-- Name: staff_position_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.staff_position_id_seq OWNED BY public.staff_position.id;


--
-- TOC entry 2721 (class 2604 OID 16423)
-- Name: genre id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.genre ALTER COLUMN id SET DEFAULT nextval('public.genre_id_seq'::regclass);


--
-- TOC entry 2720 (class 2604 OID 16415)
-- Name: movie id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.movie ALTER COLUMN id SET DEFAULT nextval('public.movie_id_seq'::regclass);


--
-- TOC entry 2723 (class 2604 OID 16455)
-- Name: position id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."position" ALTER COLUMN id SET DEFAULT nextval('public.position_id_seq'::regclass);


--
-- TOC entry 2722 (class 2604 OID 16444)
-- Name: staff id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.staff ALTER COLUMN id SET DEFAULT nextval('public.staff_id_seq'::regclass);


--
-- TOC entry 2724 (class 2604 OID 16463)
-- Name: staff_position id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.staff_position ALTER COLUMN id SET DEFAULT nextval('public.staff_position_id_seq'::regclass);


--
-- TOC entry 2876 (class 0 OID 16420)
-- Dependencies: 205
-- Data for Name: genre; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.genre (id, name) VALUES (1, 'drama');
INSERT INTO public.genre (id, name) VALUES (2, 'family');
INSERT INTO public.genre (id, name) VALUES (3, 'comedy');
INSERT INTO public.genre (id, name) VALUES (4, 'melodrama');


--
-- TOC entry 2874 (class 0 OID 16412)
-- Dependencies: 203
-- Data for Name: movie; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.movie (id, title, year) VALUES (1, 'The Green Mile', '1994');
INSERT INTO public.movie (id, title, year) VALUES (2, 'Hachi:A Dogs Tale', '2009');
INSERT INTO public.movie (id, title, year) VALUES (3, 'Forrest Gump', '1994');


--
-- TOC entry 2877 (class 0 OID 16426)
-- Dependencies: 206
-- Data for Name: movie_genre; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.movie_genre (movie_id, genre_id) VALUES (1, 1);
INSERT INTO public.movie_genre (movie_id, genre_id) VALUES (2, 1);
INSERT INTO public.movie_genre (movie_id, genre_id) VALUES (2, 2);
INSERT INTO public.movie_genre (movie_id, genre_id) VALUES (3, 1);
INSERT INTO public.movie_genre (movie_id, genre_id) VALUES (3, 3);
INSERT INTO public.movie_genre (movie_id, genre_id) VALUES (3, 4);


--
-- TOC entry 2884 (class 0 OID 16476)
-- Dependencies: 213
-- Data for Name: movie_staff; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.movie_staff (movie_id, staff_position_id) VALUES (1, 1);
INSERT INTO public.movie_staff (movie_id, staff_position_id) VALUES (1, 2);
INSERT INTO public.movie_staff (movie_id, staff_position_id) VALUES (1, 3);
INSERT INTO public.movie_staff (movie_id, staff_position_id) VALUES (1, 4);
INSERT INTO public.movie_staff (movie_id, staff_position_id) VALUES (1, 5);
INSERT INTO public.movie_staff (movie_id, staff_position_id) VALUES (2, 6);
INSERT INTO public.movie_staff (movie_id, staff_position_id) VALUES (2, 7);
INSERT INTO public.movie_staff (movie_id, staff_position_id) VALUES (2, 8);
INSERT INTO public.movie_staff (movie_id, staff_position_id) VALUES (2, 9);
INSERT INTO public.movie_staff (movie_id, staff_position_id) VALUES (3, 2);
INSERT INTO public.movie_staff (movie_id, staff_position_id) VALUES (3, 10);
INSERT INTO public.movie_staff (movie_id, staff_position_id) VALUES (3, 11);
INSERT INTO public.movie_staff (movie_id, staff_position_id) VALUES (3, 12);
INSERT INTO public.movie_staff (movie_id, staff_position_id) VALUES (3, 13);


--
-- TOC entry 2881 (class 0 OID 16452)
-- Dependencies: 210
-- Data for Name: position; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public."position" (id, name) VALUES (1, 'director');
INSERT INTO public."position" (id, name) VALUES (2, 'actor');


--
-- TOC entry 2879 (class 0 OID 16441)
-- Dependencies: 208
-- Data for Name: staff; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.staff (id, name, surname) VALUES (1, 'Frank', 'Darabont');
INSERT INTO public.staff (id, name, surname) VALUES (2, 'Tom', 'Hanks');
INSERT INTO public.staff (id, name, surname) VALUES (3, 'Barry', 'Pepper');
INSERT INTO public.staff (id, name, surname) VALUES (4, 'David', 'Morse');
INSERT INTO public.staff (id, name, surname) VALUES (5, 'Bonnie', 'Hunt');
INSERT INTO public.staff (id, name, surname) VALUES (6, 'Lasse', 'Hallstrem');
INSERT INTO public.staff (id, name, surname) VALUES (7, 'Richard', 'Gere');
INSERT INTO public.staff (id, name, surname) VALUES (8, 'Joan', 'Allen');
INSERT INTO public.staff (id, name, surname) VALUES (9, 'Jason', 'Alexander');
INSERT INTO public.staff (id, name, surname) VALUES (10, 'Robert', 'Zemeckis');
INSERT INTO public.staff (id, name, surname) VALUES (11, 'Robin', 'Wright');
INSERT INTO public.staff (id, name, surname) VALUES (12, 'Gary', 'Sinise');
INSERT INTO public.staff (id, name, surname) VALUES (13, 'Michael', 'Williamson');


--
-- TOC entry 2883 (class 0 OID 16460)
-- Dependencies: 212
-- Data for Name: staff_position; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.staff_position (id, staff_id, position_id) VALUES (1, 1, 1);
INSERT INTO public.staff_position (id, staff_id, position_id) VALUES (2, 2, 2);
INSERT INTO public.staff_position (id, staff_id, position_id) VALUES (3, 3, 2);
INSERT INTO public.staff_position (id, staff_id, position_id) VALUES (4, 4, 2);
INSERT INTO public.staff_position (id, staff_id, position_id) VALUES (5, 5, 2);
INSERT INTO public.staff_position (id, staff_id, position_id) VALUES (6, 6, 1);
INSERT INTO public.staff_position (id, staff_id, position_id) VALUES (7, 7, 2);
INSERT INTO public.staff_position (id, staff_id, position_id) VALUES (8, 8, 2);
INSERT INTO public.staff_position (id, staff_id, position_id) VALUES (9, 9, 2);
INSERT INTO public.staff_position (id, staff_id, position_id) VALUES (10, 10, 1);
INSERT INTO public.staff_position (id, staff_id, position_id) VALUES (11, 11, 2);
INSERT INTO public.staff_position (id, staff_id, position_id) VALUES (12, 12, 2);
INSERT INTO public.staff_position (id, staff_id, position_id) VALUES (13, 13, 2);


--
-- TOC entry 2895 (class 0 OID 0)
-- Dependencies: 204
-- Name: genre_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.genre_id_seq', 4, true);


--
-- TOC entry 2896 (class 0 OID 0)
-- Dependencies: 202
-- Name: movie_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.movie_id_seq', 3, true);


--
-- TOC entry 2897 (class 0 OID 0)
-- Dependencies: 209
-- Name: position_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.position_id_seq', 2, true);


--
-- TOC entry 2898 (class 0 OID 0)
-- Dependencies: 207
-- Name: staff_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.staff_id_seq', 13, true);


--
-- TOC entry 2899 (class 0 OID 0)
-- Dependencies: 211
-- Name: staff_position_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.staff_position_id_seq', 13, true);


--
-- TOC entry 2728 (class 2606 OID 16490)
-- Name: genre genre_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.genre
    ADD CONSTRAINT genre_name_key UNIQUE (name);


--
-- TOC entry 2730 (class 2606 OID 16425)
-- Name: genre genre_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.genre
    ADD CONSTRAINT genre_pkey PRIMARY KEY (id);


--
-- TOC entry 2726 (class 2606 OID 16417)
-- Name: movie movie_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.movie
    ADD CONSTRAINT movie_pkey PRIMARY KEY (id);


--
-- TOC entry 2736 (class 2606 OID 16492)
-- Name: position position_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."position"
    ADD CONSTRAINT position_name_key UNIQUE (name);


--
-- TOC entry 2738 (class 2606 OID 16457)
-- Name: position position_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."position"
    ADD CONSTRAINT position_pkey PRIMARY KEY (id);


--
-- TOC entry 2732 (class 2606 OID 16449)
-- Name: staff staff_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.staff
    ADD CONSTRAINT staff_pkey PRIMARY KEY (id);


--
-- TOC entry 2740 (class 2606 OID 16465)
-- Name: staff_position staff_position_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.staff_position
    ADD CONSTRAINT staff_position_pkey PRIMARY KEY (id);


--
-- TOC entry 2734 (class 2606 OID 16494)
-- Name: staff uc_staff; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.staff
    ADD CONSTRAINT uc_staff UNIQUE (name, surname);


--
-- TOC entry 2742 (class 2606 OID 16434)
-- Name: movie_genre movie_genre_genre_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.movie_genre
    ADD CONSTRAINT movie_genre_genre_id_fkey FOREIGN KEY (genre_id) REFERENCES public.genre(id);


--
-- TOC entry 2741 (class 2606 OID 16429)
-- Name: movie_genre movie_genre_movie_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.movie_genre
    ADD CONSTRAINT movie_genre_movie_id_fkey FOREIGN KEY (movie_id) REFERENCES public.movie(id);


--
-- TOC entry 2745 (class 2606 OID 16479)
-- Name: movie_staff movie_staff_movie_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.movie_staff
    ADD CONSTRAINT movie_staff_movie_id_fkey FOREIGN KEY (movie_id) REFERENCES public.movie(id);


--
-- TOC entry 2746 (class 2606 OID 16484)
-- Name: movie_staff movie_staff_staff_position_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.movie_staff
    ADD CONSTRAINT movie_staff_staff_position_id_fkey FOREIGN KEY (staff_position_id) REFERENCES public.staff_position(id);


--
-- TOC entry 2744 (class 2606 OID 16471)
-- Name: staff_position staff_position_position_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.staff_position
    ADD CONSTRAINT staff_position_position_id_fkey FOREIGN KEY (position_id) REFERENCES public."position"(id);


--
-- TOC entry 2743 (class 2606 OID 16466)
-- Name: staff_position staff_position_staff_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.staff_position
    ADD CONSTRAINT staff_position_staff_id_fkey FOREIGN KEY (staff_id) REFERENCES public.staff(id);


-- Completed on 2022-08-19 15:49:57

--
-- PostgreSQL database dump complete
--

