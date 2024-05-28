# Oylama-App

Oylama-App, kullanıcıların kayıt olabileceği, giriş yapabileceği ve çeşitli anket veya oylama etkinliklerine katılabileceği bir oylama platformu sağlamak için Django ile oluşturulmuş bir web uygulamasıdır.

## Kurulum

Projeyi geliştirme ve test amaçlı olarak yerel makinenizde çalıştırmak için aşağıdaki adımları izleyin:

### Kurulum Adımları

1. **Depoyu Kopyalayın**

   ```bash
   git clone https://github.com/catikonur/Oylama-App.git
   cd Oylama-App
   ```

2. **Sanal Ortam Oluşturun**

   ```bash
   python3 -m venv env
   source env/bin/activate  # Windows için `env\Scripts\activate` kullanın
   ```

3. **Bağımlılıkları Yükleyin**

   ```bash
   pip install -r requirements.txt
   ```

4. **Migrasyonları Uygulayın**

   ```bash
   python manage.py migrate
   ```

5. **Bir Süper Kullanıcı Oluşturun**

   ```bash
   python manage.py createsuperuser
   ```

6. **Geliştirme Sunucusunu Çalıştırın**

   ```bash
   python manage.py runserver
   ```

   Uygulama `http://127.0.0.1:8000/` adresinde kullanılabilir olacaktır.

## Kullanım

### Uygulamayı Çalıştırma

- Sunucu çalıştıktan sonra web tarayıcınızda uygulamaya erişebilirsiniz.
- Yeni bir hesap oluşturun veya daha önce oluşturduğunuz süper kullanıcı kimlik bilgilerini kullanarak giriş yapın.

### Yönetici Arayüzü

Django yönetici arayüzüne `http://127.0.0.1:8000/admin/` adresinden süper kullanıcı kimlik bilgilerinizi kullanarak erişebilir ve kullanıcıları yönetebilirsiniz.

## Özellikler

- Kullanıcı Kaydı ve Kimlik Doğrulama
- Anket Oluşturma ve Katılma
- Kullanıcılar ve Anketler İçin Yönetici Paneli

## Katkıda Bulunma

Depoyu fork edin ve değişikliklerinizle bir pull request gönderin.
