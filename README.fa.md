# SpamShower

یک پروژهٔ یادگیری ماشین برای دسته‌بندی پیامک‌ها به دو گروه **اسپم (Spam)** و **عادی (Ham)**.

> این پروژه آموزشی است و مدل ممکن است اشتباه کند؛ بنابراین فیلتر اسپم کاملاً دقیقی محسوب نمی‌شود.

## امکانات
- تبدیل متن پیامک‌ها به ویژگی‌های عددی با `CountVectorizer` و `TfidfVectorizer`
- آزمایش الگوریتم‌های Decision Tree، Logistic Regression و Multinomial Naive Bayes
- ارزیابی با Accuracy، Precision، Recall، F1-score و Confusion Matrix
- پیش‌بینی اسپم یا عادی بودن یک پیام دلخواه

## نتایج

نتایج ثبت‌شده در مجموعهٔ آزمایشی فعلی:

| استخراج ویژگی | الگوریتم | Accuracy |
|---|---|---:|
| CountVectorizer | Decision Tree | 97.13٪ |
| TF-IDF | Decision Tree | 97.49٪ |
| TF-IDF | Logistic Regression | 97.27٪ |
| TF-IDF | Multinomial Naive Bayes | 96.41٪ |

این نتایج به تقسیم‌بندی فعلی داده‌ها و تنظیمات پروژه وابسته‌اند و عملکرد روی داده‌های دیگر را تضمین نمی‌کنند. برای مقایسه، Precision، Recall و F1-score را هم بررسی کنید.

### نمونهٔ ماتریس درهم‌ریختگی

در یکی از آزمایش‌ها، با ترتیب برچسب‌های `ham` و سپس `spam`، این ماتریس به دست آمد:

| برچسب واقعی \\ پیش‌بینی | ham | spam |
|---|---:|---:|
| ham | 1196 | 11 |
| spam | 29 | 157 |

Accuracy این نتیجه حدود **97.13٪** است. در این آزمایش بعضی پیام‌های اسپم اشتباهاً عادی و بعضی پیام‌های عادی اشتباهاً اسپم تشخیص داده شدند.

## پیش‌نیازها
- Python 3.10 یا نسخهٔ سازگار
- pandas
- scikit-learn
- matplotlib (برای رسم Confusion Matrix)

## نصب و اجرا

```bash
git clone https://github.com/YOUR-USERNAME/SpamShower.git
cd SpamShower
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python Anti_sms_spam.py
```

مطمئن شوید دیتاست در مسیری قرار دارد که اسکریپت انتظار دارد. پیش از بازنشر دیتاست، شرایط استفادهٔ آن را بررسی کنید.

## نمونهٔ استفاده

```text
Enter Text: Congratulations! You won a free prize!
Prediction: spam
```

پیش‌بینی دقیق به مدل آموزش‌دیده و مراحل پیش‌پردازش بستگی دارد.

## ساختار پروژه

```text
SpamShower/
├── Anti_sms_spam.py
├── README.md
├── README.fa.md
├── requirements.txt
└── .gitignore
```

اگر نام فایل‌های پروژهٔ شما متفاوت است، این ساختار را مطابق فایل‌های واقعی تغییر دهید.

## دیتاست
این پروژه از دیتاست **SMS Spam Collection** استفاده می‌کند. منبع دیتاست و هرگونه ارجاع لازم را در مستندات بنویسید و پیش از انتشار مجدد داده‌ها، شرایط فعلی آن را بررسی کنید.

## چیزهایی که یاد گرفتم
- پیش‌پردازش متن و استخراج ویژگی
- تفاوت شمارش کلمات با TF-IDF
- آموزش و مقایسهٔ الگوریتم‌های دسته‌بندی
- ارزیابی مدل با Precision، Recall، F1-score و Confusion Matrix

## زبان
- [English — README](README.md)

## سلب مسئولیت
این پروژه برای یادگیری و آزمایش ساخته شده و فیلتر امنیتی یا پیام‌رسانی آمادهٔ استفادهٔ حرفه‌ای نیست.
