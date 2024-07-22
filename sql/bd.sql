PGDMP  3    "                |         
   Final Test    16.2    16.2     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    16740 
   Final Test    DATABASE     �   CREATE DATABASE "Final Test" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_United States.1252';
    DROP DATABASE "Final Test";
                postgres    false            �            1259    16767 
   categories    TABLE     n   CREATE TABLE public.categories (
    category_id integer NOT NULL,
    category_name character varying(20)
);
    DROP TABLE public.categories;
       public         heap    postgres    false            �            1259    16766    categories_category_id_seq    SEQUENCE     �   CREATE SEQUENCE public.categories_category_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 1   DROP SEQUENCE public.categories_category_id_seq;
       public          postgres    false    217            �           0    0    categories_category_id_seq    SEQUENCE OWNED BY     Y   ALTER SEQUENCE public.categories_category_id_seq OWNED BY public.categories.category_id;
          public          postgres    false    216            �            1259    16764    category_id_seq    SEQUENCE     x   CREATE SEQUENCE public.category_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 &   DROP SEQUENCE public.category_id_seq;
       public          postgres    false            �            1259    16785    nutritional_information    TABLE     �   CREATE TABLE public.nutritional_information (
    product_id integer NOT NULL,
    protein numeric(6,2),
    carbohydrates numeric(6,2),
    fat numeric(6,2),
    fiber numeric(6,2)
);
 +   DROP TABLE public.nutritional_information;
       public         heap    postgres    false            �            1259    16774    products    TABLE     �   CREATE TABLE public.products (
    product_id integer NOT NULL,
    product_name character varying(20),
    category_id integer NOT NULL,
    calories integer,
    price numeric(8,2)
);
    DROP TABLE public.products;
       public         heap    postgres    false            �            1259    16773    products_product_id_seq    SEQUENCE     �   CREATE SEQUENCE public.products_product_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.products_product_id_seq;
       public          postgres    false    219            �           0    0    products_product_id_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public.products_product_id_seq OWNED BY public.products.product_id;
          public          postgres    false    218            $           2604    16770    categories category_id    DEFAULT     �   ALTER TABLE ONLY public.categories ALTER COLUMN category_id SET DEFAULT nextval('public.categories_category_id_seq'::regclass);
 E   ALTER TABLE public.categories ALTER COLUMN category_id DROP DEFAULT;
       public          postgres    false    216    217    217            %           2604    16777    products product_id    DEFAULT     z   ALTER TABLE ONLY public.products ALTER COLUMN product_id SET DEFAULT nextval('public.products_product_id_seq'::regclass);
 B   ALTER TABLE public.products ALTER COLUMN product_id DROP DEFAULT;
       public          postgres    false    218    219    219            �          0    16767 
   categories 
   TABLE DATA           @   COPY public.categories (category_id, category_name) FROM stdin;
    public          postgres    false    217   &       �          0    16785    nutritional_information 
   TABLE DATA           a   COPY public.nutritional_information (product_id, protein, carbohydrates, fat, fiber) FROM stdin;
    public          postgres    false    220   �       �          0    16774    products 
   TABLE DATA           Z   COPY public.products (product_id, product_name, category_id, calories, price) FROM stdin;
    public          postgres    false    219   �       �           0    0    categories_category_id_seq    SEQUENCE SET     H   SELECT pg_catalog.setval('public.categories_category_id_seq', 7, true);
          public          postgres    false    216            �           0    0    category_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.category_id_seq', 1, false);
          public          postgres    false    215            �           0    0    products_product_id_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.products_product_id_seq', 31, true);
          public          postgres    false    218            '           2606    16772    categories categories_pkey 
   CONSTRAINT     a   ALTER TABLE ONLY public.categories
    ADD CONSTRAINT categories_pkey PRIMARY KEY (category_id);
 D   ALTER TABLE ONLY public.categories DROP CONSTRAINT categories_pkey;
       public            postgres    false    217            )           2606    16779    products products_pkey 
   CONSTRAINT     \   ALTER TABLE ONLY public.products
    ADD CONSTRAINT products_pkey PRIMARY KEY (product_id);
 @   ALTER TABLE ONLY public.products DROP CONSTRAINT products_pkey;
       public            postgres    false    219            +           2606    16788 ?   nutritional_information nutritional_information_product_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.nutritional_information
    ADD CONSTRAINT nutritional_information_product_id_fkey FOREIGN KEY (product_id) REFERENCES public.products(product_id);
 i   ALTER TABLE ONLY public.nutritional_information DROP CONSTRAINT nutritional_information_product_id_fkey;
       public          postgres    false    220    4649    219            *           2606    16780 "   products products_category_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.products
    ADD CONSTRAINT products_category_id_fkey FOREIGN KEY (category_id) REFERENCES public.categories(category_id);
 L   ALTER TABLE ONLY public.products DROP CONSTRAINT products_category_id_fkey;
       public          postgres    false    4647    219    217            �   r   x�=��	�p���p����2��B$�e�"�g��m�3��wk�R�j��1n�H:1xn\H|�Ljy��U����6�U��0�������}ܕ�P{�bf�5��ݿ��M      �   3  x�mRQr!���0�
z���M؝N�y?�����i����zI��jW"�,�sN��⮵Ɏ���9!���z�d�)W�a�&�H~�":��-�%G�Uq�t����
�d�L*��u�0=,7����Baң����7� �8I�N�]�!���>u�T'��d]��qvb#����x�fA]���ёx=C�=��$l���o�~����g8>Ó����c�m"x��`��j�l����(��p���t�z����±�d0�,�6��n����Cu�]�(=ڥ�����73�{��b�l��c�o�uD      �   �  x�M�MN�@���)� ��&�]8L�`R�@Q$;��J)U�+xnĳ'��ͳ�>�����7wd):���)�-7|�°�J�x�G��>ݤ1����jU\i����[r#٠r$~�D\��CU+�?и��i�y�N�Jm�kz
X�T�Z��4E�6]qC��B�`�^'�y�;˃h�� ͒�*�d9�2⼠���*R<���(K��%�xF��Z<�Y��J�u=��7TR%�~�PZv|H3x'���ej�&~l�"K>��`��m�=*2�i9+�0���9�x���=���Oi�+J����T�*� 8�|� �o��,����:�,�4�Ri![Y	g������)��z%�I�l��Ga�J�� P0�K΋��S�Z"6�R�ī+!f��4V��;f�f��p~:� r��a�t�F�w����U�~�e��>���AQ?��N     