--
-- PostgreSQL database dump
--

-- Dumped from database version 12.12
-- Dumped by pg_dump version 12.12

-- Started on 2022-08-24 10:11:57

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
-- TOC entry 203 (class 1259 OID 16578)
-- Name: data; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.data (
    id integer NOT NULL,
    name character varying(100),
    pwd character varying(100),
    email character varying(100),
    gender character varying(20)
);


ALTER TABLE public.data OWNER TO postgres;

--
-- TOC entry 202 (class 1259 OID 16576)
-- Name: data_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.data_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.data_id_seq OWNER TO postgres;

--
-- TOC entry 2840 (class 0 OID 0)
-- Dependencies: 202
-- Name: data_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.data_id_seq OWNED BY public.data.id;


--
-- TOC entry 207 (class 1259 OID 16590)
-- Name: vocabulary; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.vocabulary (
    id integer NOT NULL,
    name character varying(255),
    info text
);


ALTER TABLE public.vocabulary OWNER TO postgres;

--
-- TOC entry 206 (class 1259 OID 16588)
-- Name: vocabulary_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.vocabulary_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.vocabulary_id_seq OWNER TO postgres;

--
-- TOC entry 2841 (class 0 OID 0)
-- Dependencies: 206
-- Name: vocabulary_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.vocabulary_id_seq OWNED BY public.vocabulary.id;


--
-- TOC entry 205 (class 1259 OID 16584)
-- Name: word; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.word (
    id integer NOT NULL,
    word character varying(255),
    vocabulary_id integer
);


ALTER TABLE public.word OWNER TO postgres;

--
-- TOC entry 204 (class 1259 OID 16582)
-- Name: word_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.word_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.word_id_seq OWNER TO postgres;

--
-- TOC entry 2842 (class 0 OID 0)
-- Dependencies: 204
-- Name: word_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.word_id_seq OWNED BY public.word.id;


--
-- TOC entry 2700 (class 2604 OID 16581)
-- Name: data id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.data ALTER COLUMN id SET DEFAULT nextval('public.data_id_seq'::regclass);


--
-- TOC entry 2702 (class 2604 OID 16593)
-- Name: vocabulary id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.vocabulary ALTER COLUMN id SET DEFAULT nextval('public.vocabulary_id_seq'::regclass);


--
-- TOC entry 2701 (class 2604 OID 16587)
-- Name: word id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.word ALTER COLUMN id SET DEFAULT nextval('public.word_id_seq'::regclass);


--
-- TOC entry 2830 (class 0 OID 16578)
-- Dependencies: 203
-- Data for Name: data; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.data (id, name, pwd, email, gender) VALUES (1, 'Vasya', '21341234qwfsdf', 'mmm@mmail.com', 'm');
INSERT INTO public.data (id, name, pwd, email, gender) VALUES (2, 'Alex', '21341234', 'mmm@gmail.com', 'm');
INSERT INTO public.data (id, name, pwd, email, gender) VALUES (3, 'Alexey', 'qq21341234Q', 'alexey@gmail.com', 'm');
INSERT INTO public.data (id, name, pwd, email, gender) VALUES (4, 'Helen', 'MarryMeeee', 'hell@gmail.com', 'f');
INSERT INTO public.data (id, name, pwd, email, gender) VALUES (5, 'Jenny', 'SmakeMyb', 'eachup@gmail.com', 'f');
INSERT INTO public.data (id, name, pwd, email, gender) VALUES (6, 'Lora', 'burn23', 'tpicks@gmail.com', 'f');


--
-- TOC entry 2834 (class 0 OID 16590)
-- Dependencies: 207
-- Data for Name: vocabulary; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.vocabulary (id, name, info) VALUES (1, 'animals', NULL);
INSERT INTO public.vocabulary (id, name, info) VALUES (2, 'school', NULL);
INSERT INTO public.vocabulary (id, name, info) VALUES (3, 'nature', NULL);
INSERT INTO public.vocabulary (id, name, info) VALUES (4, 'human', NULL);
INSERT INTO public.vocabulary (id, name, info) VALUES (5, 'SF', NULL);


--
-- TOC entry 2832 (class 0 OID 16584)
-- Dependencies: 205
-- Data for Name: word; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.word (id, word, vocabulary_id) VALUES (1, 'turtle', 1);
INSERT INTO public.word (id, word, vocabulary_id) VALUES (2, 'pig', 1);
INSERT INTO public.word (id, word, vocabulary_id) VALUES (3, 'dog', 1);
INSERT INTO public.word (id, word, vocabulary_id) VALUES (4, 'cat', 1);
INSERT INTO public.word (id, word, vocabulary_id) VALUES (5, 'lizard', 1);
INSERT INTO public.word (id, word, vocabulary_id) VALUES (6, 'cow', 1);
INSERT INTO public.word (id, word, vocabulary_id) VALUES (7, 'rabbit', 1);
INSERT INTO public.word (id, word, vocabulary_id) VALUES (8, 'frog', 1);
INSERT INTO public.word (id, word, vocabulary_id) VALUES (9, 'headgehog', 1);
INSERT INTO public.word (id, word, vocabulary_id) VALUES (10, 'goat', 1);
INSERT INTO public.word (id, word, vocabulary_id) VALUES (11, 'desk', 2);
INSERT INTO public.word (id, word, vocabulary_id) VALUES (12, 'book', 2);
INSERT INTO public.word (id, word, vocabulary_id) VALUES (13, 'chalk', 2);
INSERT INTO public.word (id, word, vocabulary_id) VALUES (14, 'pen', 2);
INSERT INTO public.word (id, word, vocabulary_id) VALUES (15, 'pencil', 2);
INSERT INTO public.word (id, word, vocabulary_id) VALUES (16, 'copybook', 2);
INSERT INTO public.word (id, word, vocabulary_id) VALUES (17, 'lesson', 2);
INSERT INTO public.word (id, word, vocabulary_id) VALUES (18, 'teacher', 2);
INSERT INTO public.word (id, word, vocabulary_id) VALUES (19, 'pupils', 2);
INSERT INTO public.word (id, word, vocabulary_id) VALUES (20, 'school', 2);
INSERT INTO public.word (id, word, vocabulary_id) VALUES (21, 'ray', 3);
INSERT INTO public.word (id, word, vocabulary_id) VALUES (22, 'thunder', 3);
INSERT INTO public.word (id, word, vocabulary_id) VALUES (23, 'sun', 3);
INSERT INTO public.word (id, word, vocabulary_id) VALUES (24, 'field', 3);
INSERT INTO public.word (id, word, vocabulary_id) VALUES (25, 'hill', 3);
INSERT INTO public.word (id, word, vocabulary_id) VALUES (26, 'mountain', 3);
INSERT INTO public.word (id, word, vocabulary_id) VALUES (27, 'river', 3);
INSERT INTO public.word (id, word, vocabulary_id) VALUES (28, 'forest', 3);
INSERT INTO public.word (id, word, vocabulary_id) VALUES (29, 'grass', 3);
INSERT INTO public.word (id, word, vocabulary_id) VALUES (30, 'rain', 3);
INSERT INTO public.word (id, word, vocabulary_id) VALUES (31, 'hair', 4);
INSERT INTO public.word (id, word, vocabulary_id) VALUES (32, 'nail', 4);
INSERT INTO public.word (id, word, vocabulary_id) VALUES (33, 'finger', 4);
INSERT INTO public.word (id, word, vocabulary_id) VALUES (34, 'eye', 4);
INSERT INTO public.word (id, word, vocabulary_id) VALUES (35, 'tooth', 4);
INSERT INTO public.word (id, word, vocabulary_id) VALUES (36, 'knee', 4);
INSERT INTO public.word (id, word, vocabulary_id) VALUES (37, 'elbow', 4);
INSERT INTO public.word (id, word, vocabulary_id) VALUES (38, 'leg', 4);
INSERT INTO public.word (id, word, vocabulary_id) VALUES (39, 'arm', 4);
INSERT INTO public.word (id, word, vocabulary_id) VALUES (40, 'head', 4);
INSERT INTO public.word (id, word, vocabulary_id) VALUES (41, 'engine', 5);
INSERT INTO public.word (id, word, vocabulary_id) VALUES (42, 'steel', 5);
INSERT INTO public.word (id, word, vocabulary_id) VALUES (43, 'power', 5);
INSERT INTO public.word (id, word, vocabulary_id) VALUES (44, 'nuclear', 5);
INSERT INTO public.word (id, word, vocabulary_id) VALUES (45, 'shotgun', 5);
INSERT INTO public.word (id, word, vocabulary_id) VALUES (46, 'laser', 5);
INSERT INTO public.word (id, word, vocabulary_id) VALUES (47, 'flight', 5);
INSERT INTO public.word (id, word, vocabulary_id) VALUES (48, 'energy', 5);
INSERT INTO public.word (id, word, vocabulary_id) VALUES (49, 'Moon', 5);
INSERT INTO public.word (id, word, vocabulary_id) VALUES (50, 'splace', 5);


--
-- TOC entry 2843 (class 0 OID 0)
-- Dependencies: 202
-- Name: data_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.data_id_seq', 6, true);


--
-- TOC entry 2844 (class 0 OID 0)
-- Dependencies: 206
-- Name: vocabulary_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.vocabulary_id_seq', 5, true);


--
-- TOC entry 2845 (class 0 OID 0)
-- Dependencies: 204
-- Name: word_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.word_id_seq', 50, true);


-- Completed on 2022-08-24 10:11:57

--
-- PostgreSQL database dump complete
--

