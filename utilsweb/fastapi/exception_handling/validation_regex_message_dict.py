VALIDATION_REGEX_MESSAGE_DICT = {
    r'^field required$': {
        'farsi': r"فیلد الزامی است."
    },
    r'^extra fields not permitted$': {
        'farsi': r"ارسال فیلد اضافی مجاز نیست."
    },
    r'^none is not an allowed value$': {
        'farsi': r"ارسال مقدار none مجاز نیست."
    },
    r'^value is not none$': {
        'farsi': r"مقدار داده شده none نیست."
    },
    r'^value is not None$': {
        'farsi': r"مقدار داده شده none نیست."
    },
    r'^value could not be parsed to a boolean$': {
        'farsi': r"مقدار داده شده قابل تبدیل به بولین نیست."
    },
    r'^byte type expected$': {
        'farsi': r"نوع بایت مورد انتظار است."
    },
    r'^value is not a valid dict$': {
        'farsi': r"دیکشنری نامعتبر است."
    },
    r'^value is not a valid email address$': {
        'farsi': r"ایمیل نامعتبر است."
    },
    r'^invalid or missing URL scheme$': {
        'farsi': r"لینک داده شده معتبر نیست."
    },
    r'^URL scheme not permitted$': {
        'farsi': r"لینک داده شده معتبر نیست."
    },
    r'^userinfo required in URL but missing$': {
        'farsi': r"اطلاعات یوزر در لینک مورد نیاز است."
    },
    r'^URL host invalid$': {
        'farsi': r"دامین نامعتبر است."
    },
    r'^URL host invalid, top level domain required$': {
        'farsi': r"دامین نامعتبر است."
    },
    r'^URL port invalid, port cannot exceed 65535$': {
        'farsi': r"پورت داده شده معتبر نیست."
    },
    r'^URL invalid, extra characters found after valid URL: (?P<extra>.+) value is not a valid enumeration member; permitted: (?P<permitted>.+)$': {
        'farsi': r"لینک داده شده معتبر نیست، مقدار داده شده \g<extra> اضافی بوده و مقادیر قابل قبول شامل این موارد است: \g<permitted>"
    },
    r'^value is not a valid integer$': {
        'farsi': r"عدد داده شده معتبر نیست."
    },
    r'^value is not a valid float$': {
        'farsi': r"عدد داده شده معتبر نیست."
    },
    r'^value is not a valid path$': {
        'farsi': r"مسیر داده شده معتبر نیست."
    },
    r'^file or directory at path "(?P<path>.+)" does not exist$': {
        'farsi': r"فایل یا فولدر در مسیر \g<path> موجود نیست"
    },
    r'^path "(?P<path>.+)" does not point to a file$': {
        'farsi': r"فایل در مسیر \g<path> موجود نیست"
    },
    r'^path "(?P<path>.+)" does not point to a directory$': {
        'farsi': r"فوادر در مسیر \g<path> موجود نیست"
    },
    r'^ensure this value contains valid import path or valid callable: (?P<error_message>.+)$': {
        'farsi': r"مطمئن شوید مقدار داده شده مسیر یا تابع معتبر باشد: \g<error_message>"
    },
    r'^value is not a valid sequence$': {
        'farsi': r"سری داده شده معتبر نیست."
    },
    r'^value is not a valid iterable$': {
        'farsi': r"مقدار داده شده قابل پیمایش نیست."
    },
    r'^value is not a valid list$': {
        'farsi': r"لیست معتبر نیست."
    },
    r'^value is not a valid set$': {
        'farsi': r"محموعه معتبر نیست."
    },
    r'^value is not a valid frozenset$': {
        'farsi': r"مقدار داده شده محموعه قابت معتبر نیست."
    },
    r'^value is not a valid deque$': {
        'farsi': r"مقدار داده شده صف دوطرفه معتبر نیست."
    },
    r'^value is not a valid tuple$': {
        'farsi': r"مقدار داده شده تاپل نیست."
    },
    r'^wrong tuple length (?P<actual_length>.+), expected (?P<expected_length>.+)$': {
        'farsi': r"طول تاپل داده شده \g<actual_length> درست نیست، مقدار \g<expected_length> مورد انتظار است."
    },
    r'^ensure this value has at least (?P<limit_value>.+) items$': {
        'farsi': r"مطمین شوید مقدار داده شده حداقل \g<limit_value> آیتم داشته باشد.."
    },
    r'^the list has duplicated items$': {
        'farsi': "لیست داده شده مقدار تکراری دارد.",
    },
    r'^ensure this value has at most (?P<limit_value>.+) items$': {
        'farsi': r"مطمین شوید مقدار داده شده حداکثر \g<limit_value> آیتم داشته باشد"
    },
    r'^ensure this value has at least (?P<limit_value>.+) characters$': {
        'farsi': r"مطمین شوید مقدار داده شده حداقل \g<limit_value> کاراکتر داشته باشد."
    },
    r'^ensure this value has at most (?P<limit_value>.+) characters$': {
        'farsi': r"مطمین شوید مقدار داده شده حداکثر \g<limit_value> کاراکتر داشته باشد."
    },
    r'^str type expected$': {
        'farsi': r".نوع متن مورد انتظار است"
    },
    r'^string does not match regex "(?P<pattern>.+)"$': {
        'farsi': r"میتن داده شده باید با این فرمت باشد: \g<pattern>"
    },
    r'^ensure this value is greater than (?P<limit_value>.+)$': {
        'farsi': r".مطمئن شوید مقدار داده شده بزرگتر از \g<limit_value> باشد."
    },
    r'^ensure this value is greater than or equal to (?P<limit_value>.+)$': {
        'farsi': r".مطمئن شوید مقدار داده شده بزرگتر یا مساوی \g<limit_value> باشد."
    },
    r'^ensure this value is less than (?P<limit_value>.+)$': {
        'farsi': r".مطمئن شوید مقدار داده شده کوچکتر از \g<limit_value> باشد."
    },
    r'^ensure this value is less than or equal to (?P<limit_value>.+)$': {
        'farsi': r".مطمئن شوید مقدار داده شده کوچکتر یا مساوی \g<limit_value> باشد."
    },
    r'^ensure this value is a finite number$': {
        'farsi': r".مطمئن شوید مقدار داده شده عدد محدودی باشد"
    },
    r'^ensure this value is a multiple of (?P<multiple_of>.+)$': {
        'farsi': r"مقدار داده شده باید مضربی از \g<multiple_of> باشد."
    },
    r'^value is not a valid decimal$': {
        'farsi': r"دسیمال داده شده معتبر نیست"
    },
    r'^ensure that there are no more than (?P<max_digits>.+) digits in total$': {
        'farsi': r"تعداد ارقام باید \g<max_digits> باشد."
    },
    r'^ensure that there are no more than (?P<decimal_places>.+) decimal places$': {
        'farsi': r"تعداد اعشار نباید بیشتر از \g<decimal_places> باشد."
    },
    r'^ensure that there are no more than (?P<whole_digits>.+) digits before the decimal point$': {
        'farsi': r" \g<whole_digits> شود.تعداد ارقام صحیح نباید بیشتر از"
    },
    r'^invalid datetime format$': {
        'farsi': r"تاریخ-زمان داده شده معتبر نیست."
    },
    r'^invalid date format$': {
        'farsi': r"تاریخ داده شده معتبر نیست."
    },
    r'^date is not in the past$': {
        'farsi': r"تاریخ داده شده نگذشته است."
    },
    r'^date is not in the future$': {
        'farsi': r"تاریخ مربوط به آینده نیست."
    },
    r'^invalid time format$': {
        'farsi': r"زمان داده شده معتبر نیست"
    },
    r'^invalid duration format$': {
        'farsi': r"طول زمان معتبر نیست."
    },
    r'^value is not a valid hashable$': {
        'farsi': r"مقدار داده شده قابل هش نیست."
    },
    r'^value is not a valid uuid$': {
        'farsi': r"مقدار داده شده uuid معتبر نیست."
    },
    r'^uuid version (?P<required_version>.+) expected$': {
        'farsi': r"ورژن uuid داده شده \g<required_version> مورد انتظار است.."
    },
    r'^instance of (?P<expected_arbitrary_type>.+) expected$': {
        'farsi': r"نمونه ای از کلاس \g<expected_arbitrary_type> مورد انتظار است.."
    },
    r'^Invalid JSON$': {
        'farsi': r"جیسون معتبر نیست."
    },
    r'^JSON object must be str, bytes or bytearray$': {
        'farsi': r"جیسون باید متن، بایت یا آرایه ای از بایت ها باشد."
    },
    r'^Invalid regular expression$': {
        'farsi': r"رجکس معتبر نیست."
    },
    r'^instance of (?P<class_name>.+), tuple or dict expected$': {
        'farsi': r"نمونه ای از تاپل، دیکشنری یا \g<class_name> مورد انتظار است."
    },
    r'^(?P<value>.+) is not callable$': {
        'farsi': r"مقدار داده شده \g<value> قابلیت صدا کردن ندارد."
    },
    r'^(?P<value>.+) is not a valid Enum instance$': {
        'farsi': r"مقدار داده شده \g<value> enum نیست"
    },
    r'^(?P<value>.+) is not a valid IntEnum instance$': {
        'farsi': r"مقدار داده شده \g<value> enum نیست"
    },
    r'^value is not a valid IPv4 or IPv6 address$': {
        'farsi': r"آی پی داده شده معتبر نیست."
    },
    r'^value is not a valid IPv4 or IPv6 interface$': {
        'farsi': r"آی پی داده شده معتبر نیست."
    },
    r'^value is not a valid IPv4 or IPv6 network$': {
        'farsi': r"آی پی داده شده معتبر نیست."
    },
    r'^value is not a valid IPv4 address$': {
        'farsi': r"آی پی داده شده معتبر نیست."
    },
    r'^value is not a valid IPv6 address$': {
        'farsi': r"آی پی داده شده معتبر نیست."
    },
    r'^value is not a valid IPv4 network$': {
        'farsi': r"آی پی داده شده معتبر نیست."
    },
    r'^value is not a valid IPv6 network$': {
        'farsi': r"آی پی داده شده معتبر نیست."
    },
    r'^value is not a valid IPv4 interface$': {
        'farsi': r"آی پی داده شده معتبر نیست."
    },
    r'^value is not a valid IPv6 interface$': {
        'farsi': r"آی پی داده شده معتبر نیست."
    },
    r'^value is not a valid color: (?P<reason>.+)$': {
        'farsi': r"رنگ داده شده معتبر نیست  \g<reason>"
    },
    r'^value is not a valid boolean$': {
        'farsi': r"بولین معتبر نیست."
    },
    r'^card number is not all digits$': {
        'farsi': r"شماره کارت باید فقط شامل اعداد باشد."
    },
    r'^card number is not luhn valid$': {
        'farsi': r"شماره کارت داده شده معتبر نیست."
    },
    r'^Length for a (?P<brand>.+) card must be (?P<required_length>.+)$': {
        'farsi': r"شماره کارت داده شده برای برند \g<brand> باید \g<required_length> شماره باشد."
    },
    r'^could not parse value and unit from byte string$': {
        'farsi': r"مقدار داده شده معتبر نیست."
    },
    r'^could not interpret byte unit: (?P<unit>.+)$': {
        'farsi': r"بایت داده شده معتبر نیست: \g<unit>"
    },
    r'^Discriminator (?P<discriminator_key>.+) is missing in value$': {
        'farsi': r" کننده  \g<discriminator_key> در مقدار داده شده پیدا نشد.جدا"
    },
    r'^No match for discriminator (?P<discriminator_key>.+) and value (?P<discriminator_value>.+) (allowed values: (?P<allowed_values>.+))$': {
        'farsi': r"مقداری برای کلید جداکننده \g<discriminator_key> و مقدار جدا کننده \g<discriminator_value> پیدا نشد (مقادیر محاز: \g<allowed_values>) ."
    },
    r'^String should have at least (?P<length>.+) characters$': {
        'farsi': r"متن باید حداقل \g<length> حرف داشته باشد.",
    },
    r'^String should have at most (?P<length>.+) characters$': {
        'farsi': r"متن میتواند حداکثر \g<length> حرف داشته باشد.",
    },
    r'^String should match pattern (?P<pattern>.+)$': {
        # 'farsi': r"متن باید متناسب با این الگو باشد: \g<pattern>",
        'farsi': r"الگوی داده شده مورد قبول نمی باشد.",
    },
    r'^Input should be a valid date or datetime, input is too short$': {
        'farsi': r"مقدار داده شده یک مقدار معتبر تاریخ و با تاریخ-زمان نیست، مقدار داده شده کوتاه است.",
    },
    r'^Input should be a valid integer, unable to parse string as an integer$': {
        'farsi': r"مقدار داده شده عدد نیست، بلکه متن است.",
    },
    r'^Input should be a valid string$': {
        'farsi': r"مقدار داده شده مقدار معتبر متنی نیست.",
    },
    r'^Input should be a valid integer$': {
        'farsi': r"مقدار داده شده عدد نیست.",
    },
}
# Input should be 'PDF', 'XLS', 'CSV', 'DOC', 'PPT', 'TXT', 'RAR', 'ZIP', 'JSON', 'MPEG', 'MP4', 'MP3' or 'WAV'"
# TODO: implement in a way that this custome messages can be added