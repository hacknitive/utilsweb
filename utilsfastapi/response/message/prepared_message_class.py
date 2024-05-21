from .message_class import Message as _Message


class Message(_Message):
    delete_parent = {
        'farsi': "آیتم داده شده نمیتواند حذف شود، زیرا در {item} استفاده شده است.",
        'english': "The given item Cannot be deleted, because it is used in {item}!",
    }

    item_not_found = {
        'farsi': "آیتم داده شده" + " '{item}' " + "پیدا نشد!",
        'english': "The given item '{item}' not found!",
    }

    item_deleted_previously = {
        'farsi': "آیتم داده شده" + " '{item}' " + "قبلا پاک شده است!",
        'english': "The item '{item}' was deleted previously!"
    }

    duplicate_item = {
        'farsi': "آیتم داده شده" + " '{item}' " + "تکراری است!",
        'english': "The given item '{item}' exist previously!"
    }

    unregistered_item = {
        'farsi': "آیتم داده شده" + " '{item}' " + "قبلا ثبت نشده است!",
        'english': "The given item '{item}' is not registered!"
    }

    invalid_value = {
        'farsi': "مقدار داده شده" + " '{value}' " + "درست (معتبر) نیست!",
        'english': "The given value '{value}' is not valid!"
    }

    invalid_value_with_reason = {
        'farsi': "مقدار داده شده" + " '{value}' " + "درست (معتبر) نیست چون" + " {reason} ",
        'english': "The given value '{value}' is not valid because '{reason}'!",
    }

    frozen_item = {
        'farsi': "آیتم داده شده" + " '{item}' " + "فریز شده است و نمیتواند پاک شود!",
        'english': "The item '{id}' is frozen and can not be deleted/updated!",
    }

    not_given_data = {
        'farsi': "داده" + " '{data}' " + "باید داده شود!",
        'english': "data '{data}' should be given!",
    }

    # file
    unacceptable_file_format = {
        'farsi': "فرمت فایل داده شده مورد قبول نیست!",
        'english': "The given file format is not acceptable!"
    }

    # User Authorization/Authentication
    not_admin_user = {
        'farsi': "شما ادمین نیستید و نمیتوانید به این آدرس" + " '{route}' " + "دسترسی داشته باشید!",
        'english': "You are not admin, so you cannot reach this route '{route}'!",
    }

    admin_user = {
        'farsi': "شما ادمین هستید و نمیتوانید به این آدرس" + " '{route}' " + "دسترسی داشته باشید!",
        'english': "You are admin, so you cannot reach this route '{}'!"
    }

    invalid_token = {
        'farsi': "توکن داده شده درست (معتبر) نیست!",
        'english': "The given token is not valid!"
    }

    expired_token = {
        'farsi': "توکن داده شده منقضی شده است!",
        'english': "The given token expired!"
    }

    invalid_password = {
        'farsi': "پسورد داده شده معتبر نیست!",
        'english': "The given password is not valid!"
    }

    no_password = {
        'farsi': "پسورد تغریف نشده است.",
        'english': "Password is not defined yet."
    }

    not_allowed = {
        'farsi': "شما مجاز به انجام این کار نیستید.",
        'english': "It is not allowed!"
    }

    unauthorized_user = {
        'farsi': "کاربر شناسایی نشده است!",
        'english': "This user is not authenticated!"
    }

    user_suspension = {
        'farsi': "کاربر معلق شده است!",
        'english': "User is suspended!"
    }

    already_registered_user = {
        'farsi': "کاربر قبلا ثبت نام کرده است!",
        'english': None
    }

    unregistered_user = {
        'farsi': "کاربر وجود ندارد!",
        'english': None
    }

    inactive_user = {
        'farsi': "کاربری شما فعال نشده است. لطفا منتظر تایید ادمین باشید.",
        'english': "User is inactive! Please wait for admin approval."
    }

    # Service Authorization/Authentication
    realm_not_found = {
        'farsi': "حوزه" + " '{realm}' " + "پیدا نشد!",
        'english': "Realm '{realm}' not found!"
    }

    unauthorized_service = {
        'farsi': "سرویس شناسایی نشد!",
        'english': "This service is not authenticated!"
    }

    # OTP
    send_otp = {
        'farsi': "کد پیامکی ارسال شده است!",
        'english': "OTP code is sent."
    }

    invalid_otp = {
        'farsi': "کد وارد شده صحیح نیست. لطفا دوباره تلاش کنید!",
        'english': "The entered code is not correct. Try again!"
    }

    time_limit_otp = {
        'farsi': "کد پیامکی به تازگی ارسال شده است. لطفا" + " '{duration}' " + "بعد تلاش کنید.",
        'english': "An otp code is sent to your phone recently. please try again {duration} later!"
    }

    otp_expired = {
        'farsi': "کد وارد شده منقضی شده است.",
        'english': "OTP code is expired."
    }

    # Server
    server_error = {
        'farsi': "خطای غیر منتظره رخ داده است!!! چند دقیقه بعد دوباره تلاش کنید."
                 "این خطا به صورت خودکار به ادمین اطلاع داده شده است!",
        'english': "A server error occurred! Keep calm! It is reported to admin automatically!"
    }

    internal_server_error = {
        'farsi': "خطای غیر منتظره رخ داده است!!! چند دقیقه بعد دوباره تلاش کنید."
                 "این خطا به صورت خودکار به ادمین اطلاع داده شده است!",
        'english': "Internal server error occurred! Keep calm! It is reported to admin automatically!"
    }

    service_unavailable = {
        'farsi': "سرویس مورد نظر" + " '{service}' "
                 + "موقتا در دسترسی نیست! این مورد به صورت خودکار به ادمین اطلاع داده شده است.",
        'english': "The service '{service}' is not available now, Keep calm! It is reported to admin automatically!"
    }

    # Common
    success_message = {
        'farsi': "عملیات موفقیت آمیز بود.",
        'english': "The operation is done successfully."
    }

    failure_message = {
        'farsi': "عملیات ناموفق بود!",
        'english': "The operation failed."
    }

    # Validation errors
    field_required = {
        'farsi': "این فیلد الزامی میباشد.",
        'english': 'field required'
    }

    extra_fields_not_permitted = {
        'farsi': "دادن فیلد اضافی ممنوع است.",
        'english': 'extra fields not permitted'
    }

    none_is_not_an_allowed_value = {
        'farsi': "مقدار" + " null " + "مورد قبول نیست.",
        'english': 'none is not an allowed value'
    }

    value_is_not_none = {
        'farsi': "مقدار" + " null " + "نیست.",
        'english': 'value is not none'
    }

    value_could_not_be_parsed_to_a_boolean = {
        'farsi': "مقدار داده شده قابل تبدیل به بولین نیست!",
        'english': 'value could not be parsed to a boolean'
    }

    byte_type_expected = {
        'farsi': "نوع بایت باید داده شود!",
        'english': 'byte type expected'
    }

    value_is_not_a_valid_dict = {
        'farsi': "آبجکت قابل قبول نیست!",
        'english': 'value is not a valid dict'
    }

    value_is_not_a_valid_email_address = {
        'farsi': "ایمیل معتبر نیست!",
        'english': 'value is not a valid email address'
    }

    invalid_or_missing_URL_scheme = {
        'farsi': "آدرس معتبر نیست!",
        'english': 'invalid or missing URL scheme'
    }

    url_scheme_not_permitted = {
        'farsi': "آدرس معتبر نیست!",
        'english': 'URL scheme not permitted'
    }

    userinfo_required_in_URL_but_missing = {
        'farsi': "اطلاعات کاربر در آدرس مورد نیاز است اما فریتاده نشده است!",
        'english': 'userinfo required in URL but missing'
    }

    url_host_invalid = {
        'farsi': "آدرس هاست نامعتبر است!",
        'english': 'URL host invalid'
    }

    url_host_invalid_top_level_domain_required = {
        'farsi': "آدرس هاست نامعتبر است، دامین مورد نیاز است.",
        'english': 'URL host invalid, top level domain required'
    }

    url_port_invalid_port_cannot_exceed_65535 = {
        'farsi': "پورت نامعتبر است، پورت باید کمتر از ۶۵۵۳۵ باشد.",
        'english': 'URL port invalid, port cannot exceed 65535'
    }

    value_is_not_a_valid_integer = {
        'farsi': "مقدار عدد صحیح نیست.",
        'english': 'value is not a valid integer'
    }

    value_is_not_a_valid_float = {
        'farsi': "مقدار عدد اعشاری نیست.",
        'english': 'value is not a valid float'
    }

    value_is_not_a_valid_path = {
        'farsi': "مقدار آدرس فایل یا فولدر نیست.",
        'english': 'value is not a valid path'
    }

    value_is_not_a_valid_sequence = {
        'farsi': "مقدار توالی از داده ها نیست.",
        'english': 'value is not a valid sequence'
    }

    value_is_not_a_valid_iterable = {
        'farsi': "مقدار قابل شمارش نیست.",
        'english': 'value is not a valid iterable'
    }

    value_is_not_a_valid_list = {
        'farsi': "مقدار داده شده لیست نیست.",
        'english': 'value is not a valid list'
    }

    value_is_not_a_valid_set = {
        'farsi': "مقدار داده شده مجموعه نیست.",
        'english': 'value is not a valid set'
    }

    value_is_not_a_valid_frozenset = {
        'farsi': "مقدار داده شده مجموعه فریزشده نیست.",
        'english': 'value is not a valid frozenset'
    }

    value_is_not_a_valid_deque = {
        'farsi': "مقدار داده شده صف دو طرفه نیست.",
        'english': 'value is not a valid deque'
    }

    value_is_not_a_valid_tuple = {
        'farsi': "مقدار داده شده تاپل نیست.",
        'english': 'value is not a valid tuple'
    }

    the_list_has_duplicated_items = {
        'farsi': "لیست داده شده دارای مقدار تکراری است.",
        'english': 'the list has duplicated items'
    }

    str_type_expected = {
        'farsi': "رشته متنی مورد نظر است.",
        'english': 'str type expected'
    }

    ensure_this_value_is_a_finite_number = {
        'farsi': "مطمپن شوید که یک مقدار متناهی وارد میکنید.",
        'english': 'ensure this value is a finite number'
    }

    value_is_not_a_valid_decimal = {
        'farsi': "مقدار داده شده دسیمال نیست.",
        'english': 'value is not a valid decimal'
    }

    invalid_datetime_format = {
        'farsi': "فرمت تاریخ و زمان معتبر نیست.",
        'english': 'invalid datetime format'
    }

    invalid_date_format = {
        'farsi': "فرمت تاریخ معتبر نیست.",
        'english': 'invalid date format'
    }

    date_is_not_in_the_past = {
        'farsi': "تاریخ باید مربوط به گذشته باشد.",
        'english': 'date is not in the past'
    }

    date_is_not_in_the_future = {
        'farsi': "تاریخ در مورد آینده نیست.",
        'english': 'date is not in the future'
    }

    invalid_time_format = {
        'farsi': "زمان داده شده معتبر نیست.",
        'english': 'invalid time format'
    }

    invalid_duration_format = {
        'farsi': "بازه زمانی داده شده معتبر نیست.",
        'english': 'invalid duration format'
    }

    value_is_not_a_valid_hashable = {
        'farsi': "مقدار داده شده قابل هش نیست.",
        'english': 'value is not a valid hashable'
    }

    value_is_not_a_valid_uuid = {
        'farsi': "مقدار داده شده uuid معتبر نیست",
        'english': 'value is not a valid uuid'
    }

    a_class_is_expected = {
        'farsi': "کلاس مورد انظار است.",
        'english': 'a class is expected'
    }

    invalid_json = {
        'farsi': "JSON معتبر نیست.",
        'english': 'Invalid JSON'
    }

    json_object_must_be_str_bytes_or_bytearray = {
        'farsi': "JSON باید متن، بایت و یا آرایه ای از بایت ها باشد.",
        'english': 'JSON object must be str, bytes or bytearray'
    }

    invalid_regular_expression = {
        'farsi': "عبارات با قاعده (regex) معتبر نیست.",
        'english': 'Invalid regular expression'
    }

    value_is_not_a_valid_ipv4_or_ipv6_address = {
        'farsi': "مقدار داده شده IPv4 یا IPv6 معتبر نیست.",
        'english': 'value is not a valid IPv4 or IPv6 address'
    }

    value_is_not_a_valid_ipv4_or_ipv6_interface = {
        'farsi': "مقدار داده شده IPv4 یا IPv6 معتبر نیست.",
        'english': 'value is not a valid IPv4 or IPv6 interface'
    }

    value_is_not_a_valid_ipv4_or_ipv6_network = {
        'farsi': "مقدار داده شده IPv4 یا IPv6 معتبر نیست.",
        'english': 'value is not a valid IPv4 or IPv6 network'
    }

    value_is_not_a_valid_ipv4_address = {
        'farsi': "مقدار داده شده IPv4 معتبر نیست.",
        'english': 'value is not a valid IPv4 address'
    }

    value_is_not_a_valid_ipv6_address = {
        'farsi': "مقدار داده شده IPv6 معتبر نیست.",
        'english': 'value is not a valid IPv6 address'
    }

    value_is_not_a_valid_ipv4_network = {
        'farsi': "مقدار داده شده IPv4 معتبر نیست.",
        'english': 'value is not a valid IPv4 network'
    }

    value_is_not_a_valid_ipv6_network = {
        'farsi': "مقدار داده شده IPv6 معتبر نیست.",
        'english': 'value is not a valid IPv6 network'
    }

    value_is_not_a_valid_ipv4_interface = {
        'farsi': "مقدار داده شده IPv4 معتبر نیست.",
        'english': 'value is not a valid IPv4 interface'
    }

    value_is_not_a_valid_ipv6_interface = {
        'farsi': "مقدار داده شده IPv6 معتبر نیست.",
        'english': 'value is not a valid IPv6 interface'
    }

    value_is_not_a_valid_boolean = {
        'farsi': "مقدار داده شده بولین معتبر نیست.",
        'english': 'value is not a valid boolean'
    }

    card_number_is_not_all_digits = {
        'farsi': "شماره کارت باید تماما عدد باشد.",
        'english': 'card number is not all digits'
    }

    card_number_is_not_luhn_valid = {
        'farsi': "شماره کارت معتبر نیست.",
        'english': 'card number is not luhn valid'
    }

    could_not_parse_value_and_unit_from_byte_string = {
        'farsi': "بایت داده شده قابل تفسیر کردن نیست.",
        'english': 'could not parse value and unit from byte string'
    }
