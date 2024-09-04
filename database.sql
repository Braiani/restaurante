-- Remover o banco de dados existente e criar um novo
drop database if exists pythonapps;
create database if not exists pythonapps;
use pythonapps;

-- Criar a tabela users
create table users (
    id int auto_increment primary key,
    username varchar(100) not null,
    name varchar(255) not null,
    password varchar(100) not null
);

insert into users (username, name, password) values 
    ("ederson", "Ederson", "123456"), 
    ("edini", "Edini", "123456"), 
    ("enilda", "Enilda", "123456");

-- Criar a tabela categories
create table categories (
    id int auto_increment primary key,
    description varchar(100) not null
);

-- Criar a tabela products com um campo de imagem em Base64
create table products (
    id int auto_increment primary key,
    description varchar(100) not null,
    price float not null,
    category_id int not null,
    image text,  -- Alterado nome do campo de image_base64 para image
    constraint foreign key (category_id) references categories(id)
);

-- Criar a tabela cart
create table cart (
    id int auto_increment primary key,
    product_id int not null,
    quantity int default(1),
    status enum('open', 'closed') default('open'),
    constraint foreign key (product_id) references products(id)
);

-- Inserir categorias
INSERT INTO categories (description) VALUES
    ('Entradas'),
    ('Pratos Principais'),
    ('Bebidas'),
    ('Bebidas Alcoólicas'),
    ('Sobremesas'),
    ('Menu do Chef');

-- Inserir produtos para a categoria 'Entradas'
INSERT INTO products (description, price, category_id, image) VALUES
    ('Bruschetta', 12.50, (SELECT id FROM categories WHERE description = 'Entradas'), "https://cloudfront-us-east-1.images.arcpublishing.com/estadao/3MOX4CLWZVFHDKSRKXZFHO24EU.jpg"),
    ('Crostini', 15.00, (SELECT id FROM categories WHERE description = 'Entradas'), "https://www.hiddenvalley.com/wp-content/uploads/2021/04/ranch-club-crostini-RDP.jpg"),
    ('Azeitonas Temperadas', 8.00, (SELECT id FROM categories WHERE description = 'Entradas'), "https://1.bp.blogspot.com/-mUzXX-9b6vQ/XR3NFrHkHwI/AAAAAAAAGeg/ELa-iALg7RU7i7GAS2nXlaY7TTmBS5HIACLcBGAs/s1600/20190704_103230.jpg"),
    ('Salada Caprese', 14.00, (SELECT id FROM categories WHERE description = 'Entradas'), "https://s2-receitas.glbimg.com/g8xJERPO0rD8arQTLRw7hogSU_A=/0x0:690x460/984x0/smart/filters:strip_icc()/s.glbimg.com/po/rc/media/2013/11/29/16_28_16_103_Salada_Caprese_Faby_c_pia.jpg"),
    ('Sopa de Tomate', 11.00, (SELECT id FROM categories WHERE description = 'Entradas'), "https://www.comidaereceitas.com.br/wp-content/uploads/2020/07/sopa_tomates.jpg");

-- Inserir produtos para a categoria 'Pratos Principais'
INSERT INTO products (description, price, category_id, image) VALUES
    ('Filé Mignon', 45.00, (SELECT id FROM categories WHERE description = 'Pratos Principais'), "https://irp.cdn-website.com/33406c6e/dms3rep/multi/fil%C3%A9_mignon-6ad2b469.jpg"),
    ('Risoto de Cogumelos', 38.00, (SELECT id FROM categories WHERE description = 'Pratos Principais'), "https://www.comidaereceitas.com.br/wp-content/uploads/2008/10/Risoto-de-cogumelos-freepik.jpg"),
    ('Espaguete à Carbonara', 32.00, (SELECT id FROM categories WHERE description = 'Pratos Principais'), "https://painacozinha.com/wp-content/uploads/79.Espaguete-a-Carbonara.webp"),
    ('Peito de Frango Grelhado', 28.00, (SELECT id FROM categories WHERE description = 'Pratos Principais'), "https://catracalivre.com.br/cdn-cgi/image/f=auto,q=60,width=1080,height=99999,fit=scale-down/wp-content/uploads/2023/10/peito-frango-grelhado.jpg"),
    ('Salmão ao Molho de Limão', 42.00, (SELECT id FROM categories WHERE description = 'Pratos Principais'), "https://www.mococa.com.br/wp-content/uploads/2022/03/Salmao-grelhao-ao-molho-de-limao.jpeg");

-- Inserir produtos para a categoria 'Bebidas'
INSERT INTO products (description, price, category_id, image) VALUES
    ('Água Mineral', 5.00, (SELECT id FROM categories WHERE description = 'Bebidas'), "https://aguasprata.vteximg.com.br/arquivos/ids/156956-850-1000/AGUA-MINERAL-COM-GAS-PRATA-OW-PILFER-300mL.jpg"),
    ('Refrigerante', 6.00, (SELECT id FROM categories WHERE description = 'Bebidas'), "https://yorkgrill.com.br/wp-content/uploads/2022/06/refrigerante.png"),
    ('Suco de Laranja', 7.00, (SELECT id FROM categories WHERE description = 'Bebidas'), "https://s2.glbimg.com/E1WXXtiXeTi1DyT5Y1O3uf2DICs=/e.glbimg.com/og/ed/f/original/2019/01/15/31617293018_896bf29d55_k.jpg"),
    ('Chá Gelado', 6.50, (SELECT id FROM categories WHERE description = 'Bebidas'), "https://s2-receitas.glbimg.com/km_FlDuJuzPqoweqqh04Jm08aMk=/0x0:338x507/984x0/smart/filters:strip_icc()/s.glbimg.com/po/rc/media/2014/01/03/14_05_20_789_ch_gelado_04.jpg"),
    ('Água de Coco', 8.00, (SELECT id FROM categories WHERE description = 'Bebidas'), "https://p2.trrsf.com/image/fget/cf/774/0/images.terra.com/2023/01/11/27273641-agua-de-coco-1.jpg");

-- Inserir produtos para a categoria 'Bebidas Alcoólicas'
INSERT INTO products (description, price, category_id, image) VALUES
    ('Cerveja Artesanal', 10.00, (SELECT id FROM categories WHERE description = 'Bebidas Alcoólicas'), "https://cervejariaantuerpia.com.br/wp-content/uploads/2021/08/CERVEJA-ARTESANAL.jpg"),
    ('Vinho Tinto', 45.00, (SELECT id FROM categories WHERE description = 'Bebidas Alcoólicas'), "https://cdn.dooca.store/197/products/kit-tintos-suaves-mais-vendidos-6-garrafas_450x600+fill_ffffff.jpg"),
    ('Vinho Branco', 40.00, (SELECT id FROM categories WHERE description = 'Bebidas Alcoólicas'), "https://acdn.mitiendanube.com/stores/002/826/384/products/vinho-branco-suave-rio-valley-750ml1-27a8b0288f138f85af16919466780951-1024-1024.png"),
    ('Whisky', 80.00, (SELECT id FROM categories WHERE description = 'Bebidas Alcoólicas'), "https://dcdn.mitiendanube.com/stores/002/905/426/products/341631-whisky-johnnie-walker-18-anos-750ml-067c969be0ef23daca16970779662191-640-0.jpg"),
    ('Margarita', 15.00, (SELECT id FROM categories WHERE description = 'Bebidas Alcoólicas'), "https://assets.tmecosys.com/image/upload/t_web767x639/img/recipe/ras/Assets/432923A3-27F5-40D7-BDEE-1D41C59A67D2/Derivates/94A69FFC-EEF4-4165-AF13-518881F611F3.jpg");

-- Inserir produtos para a categoria 'Sobremesas'
INSERT INTO products (description, price, category_id, image) VALUES
    ('Cheesecake', 12.00, (SELECT id FROM categories WHERE description = 'Sobremesas'), "https://static.itdg.com.br/images/360-240/722816207b46644920ab0c65a7faab72/shutterstock-2202992931.jpg"),
    ('Tiramisu', 14.00, (SELECT id FROM categories WHERE description = 'Sobremesas'), "https://cloudfront-us-east-1.images.arcpublishing.com/estadao/Q3SE72ZUZRGKHOJHHW33TBLP4A.jpg"),
    ('Brownie com Sorvete', 13.00, (SELECT id FROM categories WHERE description = 'Sobremesas'), "https://ogimg.infoglobo.com.br/in/23710215-4a4-e80/FT1086A/82919017_BAToque-de-Chef-restaurante-Barsa.-Receita-Brownie-com-sorvete-de-creme-e-calda-de-c.jpg"),
    ('Mousse de Chocolate', 11.00, (SELECT id FROM categories WHERE description = 'Sobremesas'), "https://cdn0.tudoreceitas.com/pt/posts/6/3/3/mousse_de_chocolate_light_cremosa_7336_orig.jpg"),
    ('Pavê de Frutas', 10.00, (SELECT id FROM categories WHERE description = 'Sobremesas'), "https://i.ytimg.com/vi/3Tw_bfJGWqU/maxresdefault.jpg");

-- Inserir produtos para a categoria 'Menu do Chef'
INSERT INTO products (description, price, category_id, image) VALUES
    ('Prato do Dia', 50.00, (SELECT id FROM categories WHERE description = 'Menu do Chef'), "https://vejasp.abril.com.br/wp-content/uploads/2016/12/ambar_almoc3a7oviradopaulista-22-de-24-jpeg.jpg"),
    ('Menu Degustação', 75.00, (SELECT id FROM categories WHERE description = 'Menu do Chef'), "https://cloudfront-us-east-1.images.arcpublishing.com/estadao/PJOK7DJXJVONNN3LOOVFVAW6E4.jpg"),
    ('Especialidade do Chef', 60.00, (SELECT id FROM categories WHERE description = 'Menu do Chef'), "https://media-cdn.tripadvisor.com/media/photo-s/1a/e4/5a/a0/especialidade-do-chef.jpg"),
    ('Menu Executivo', 45.00, (SELECT id FROM categories WHERE description = 'Menu do Chef'), "https://mcities.com.br/curitiba/wp-content/uploads/sites/3/2017/09/Menu-Executivo_Pobre-Juan-5.jpeg"),
    ('Jantar Romântico', 85.00, (SELECT id FROM categories WHERE description = 'Menu do Chef'), "https://i0.wp.com/terroirboccati.com.br/wp-content/uploads/2021/06/Falling-For-You___.jpg");
