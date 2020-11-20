## Тестовое задание на позицию Backend разработчик в [Apptrix](https://apptrix.ru/)

#### Установка Docker
* [Подробное руководство по установке docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/)

#### Установка docker-compose

* [Подробное руководство по установке docker-compose](https://docs.docker.com/compose/install/)

### Запуск
Запуск производится командой
```sh
$ docker-compose up

```
### Работа с сервисом
Сервер работает на `http://localhost`

### Эндпоинты:

**Регистрация пользователей**  

+ Метод: **POST** `http://localhost/api/user/`

    + Аргументы:  
	`username` : имя пользователя.    
	`email` : адрес электронной почты, на который придет подтверждение (активация аккаунта).    
	`password` : пароль пользователя.   
    
    + Ответ:  
	`username`: имя пользователя.   
	`email`: адрес электронной почты пользователя.  
	`token`: токен пользователя.    
    
**Подтверждение пользователей**

+ Метод: **GET** `http://localhost/<int:pk>/<str:token>/`

    + Ссылка генерируется автоматически и отправляется пользователям по почте
    + `<int:pk>` - номер пользователя
    + `<str:token>` - токен пользователя

   
### Управление контентом    
+ Производится из административной панели Django по адресу `http://localhost/admin` с помощью моделей:  

    + `Top background` images - фото верхнего фона лендинга 
    + `Item models` - управление товарами, отображающимися на лендинге  
    + `Block3 images` - управление фото третьего блока  
    + `Reviewss` - управление отзывами  
    + `Contactss` - управление контактами в футере  
