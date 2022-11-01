импорт   единицы измерения
из   общего общего   импорта  
из   dns   импортировать  dns 


Класс   TestDns ( unittest . Тестовый пример ):
    "" "Тест: записи в пустой базе данных" ""
    определение   test_empty_dns (self):
        DnsRecursive  =  d1 ()
        Компьютер  =   cd1 ( "cd1")
        cd1 . get_service ( d1 )
        d1 . set_host ( cd1 )
        d1  =   результат . db . num_records ()
        self . assertEqual ( результат, 0 )

    "" "Тест: добавление записи в базу данных" ""
    test_add_dns_record   определение ( self ):
        DnsRecursive  =  d1 ()
        Компьютер  =   cd1 ( "cd1")
        cd1 . get_service ( d1 )
        d1 . set_host ( cd1 )
        d1 . db . form_record ( "ya.ru " , "10.20.30.40" )
        d1  =   результат . db . num_records ()
        self . assertEqual ( результат, 1 )

    "" "Тест: удаление записи из базы данных" ""
    test_delete_dns_record   определение ( self ):
        DnsRecursive  =  d1 ()
        Компьютер  =   cd1 ( "cd1")
        cd1 . get_service ( d1 )
        d1 . set_host ( cd1 )
        d1 . db . form_record ( "ya.ru " , "10.20.30.40" )
        d1  =   результат . db . num_records ()
        self . assertEqual ( результат, 1 )
        d1 . db . delete_record ( "ya.ru " )
        d1  =   результат . db . num_records ()
        self . assertEqual ( результат, 0 )

    "" "Тест: рекурсивное разрешение имени из пустых баз данных" ""
    test_resolve_blank_dns_   рекурсивное определение (self):
        Компьютер  =  comp1 ( "Первый" )
        DnsRecursive  =  d1 ()
        DnsRecursive  =  d2 ()
        d1 . set_dns ( "8.8.4.4" )
        Компьютер  =   cd1 ( "cd1")
        cd1 . get_service ( d1 )
        Компьютер  =  cd2 ( "cd2" )
        cd2 . get_service ( d2 )
        d1 . set_host ( cd1 )
        d2 . set_host ( cd2 ) установить хост ( cd2 )
        Сеть   =  сеть ()
        net . set_dns ( "8.8.8.8" )
        net . add_host ( comp1, "172.10.10.1" )
        comp1 . get_interface (). get_dns ()
        net . add_host ( cd1, "8.8.8.8")
        net . add_host ( cd2, "8.8.4.4")
        comp1  =  результат . разрешить ( "любой")
        self . assertEqual ( результат, "Неизвестный хост" )

    "" "Тест: рекурсивное преобразование имени из первой базы данных" ""
    test_resolve_1st_dns_   рекурсивное определение (self):
        Компьютер  =   comp1 ("Первый")
        DnsRecursive  =  d1 ()
        DnsRecursive  =  d2 ()
        d1 . set_dns ( "8.8.4.4" )
        Компьютер  =   cd1 ( "cd1")
        cd1 . get_service ( d1 )
        Компьютер  =  cd2 ( "cd2")
        cd2 . get_service ( d2 )
        d1 . set_host ( cd1 )
        d2 . set_host ( cd2)
        Сеть   =  сеть ()
        net . set_dns ( "8.8.8.8" )
        net . add_host ( comp1, "172.10.10.1" )
        comp1 . get_interface (). get_dns ()
        net . add_host ( cd1, "8.8.8.8")
        net . add_host ( cd2, "8.8.4.4")
        d1 . db . form_record ( "google.com " , "1.2.3.4" )
        comp1  =  результат . разрешить ( "google.com " )
        self . assertEqual ( результат, "1.2.3.4" )

    "" "Тест: рекурсивное разрешение имени из второй базы данных" ""
    test_resolve_2nd_dns_   рекурсивное определение (self):
        Компьютер  =   comp1 ("Первый")
        DnsRecursive  =  d1 ()
        DnsRecursive  =  d2 ()
        d1 . set_dns ( "8.8.4.4" )
        Компьютер  =   cd1 ( "cd1")
        cd1 . get_service ( d1 )
        Компьютер  =  cd2 ( "cd2")
        cd2 . get_service ( d2 )
        d1 . set_host ( cd1 )
        d2 . set_host ( cd2)
        Сеть   =  сеть ()
        net . set_dns ( "8.8.8.8" )
        net . add_host ( comp1, "172.10.10.1" )
        comp1 . get_interface (). get_dns ()
        net . add_host ( cd1, "8.8.8.8")
        net . add_host ( cd2, "8.8.4.4")
        d2 . db . form_record ( "google.com " , "1.2.3.4" )
        comp1  =  результат . разрешить ( "google.com " )
        self . assertEqual ( результат, "1.2.3.4" )

    "" "Тест: нерекурсивное разрешение имени из пустых баз данных" ""
    test_resolve_blank_dns_nonrecursive   определение ( self):
        Компьютер  =   comp1 ("Первый")
        DnsNonRecursive  =  d1 ()
        DnsNonRecursive  =  d2 ()
        d1 . set_dns ( "8.8.4.4" )
        Компьютер  =   cd1 ( "cd1")
        cd1 . get_service ( d1 )
        Компьютер  =  cd2 ( "cd2")
        cd2 . get_service ( d2 )
        d1 . set_host ( cd1 )
        d2 . set_host ( cd2)
        Сеть   =  сеть ()
        net . set_dns ( "8.8.8.8" )
        net . add_host ( comp1, "172.10.10.1" )
        comp1 . get_interface (). get_dns ()
        net . add_host ( cd1, "8.8.8.8")
        net . add_host ( cd2, "8.8.4.4")
        comp1  =  результат . разрешить ( "любой")
        self . assertEqual ( результат, "Неизвестный хост" )

    "" "Тест: нерекурсивное разрешение имени из первой базы данных" ""
    test_resolve_1st_dns_nonrecursive   определение ( self):
        Компьютер  =   comp1 ("Первый")
        DnsNonRecursive  =  d1 ()
        DnsNonRecursive  =  d2 ()
        d1 . set_dns ( "8.8.4.4" )
        Компьютер  =   cd1 ( "cd1")
        cd1 . get_service ( d1 )
        Компьютер  =  cd2 ( "cd2")
        cd2 . get_service ( d2 )
        <span>d1</span> . <span>set_host</span> ( <span>cd1</span> )
        d2 . set_host ( cd2 )
        net  =  Network ()
        net . set_dns ( "8.8.8.8" )
        net . add_host ( comp1 , "172.10.10.1" )
        comp1 . get_interface (). get_dns ()
        net . add_host ( cd1 , "8.8.8.8" )
        net . add_host ( cd2, "8.8.4.4")
        d1 . db . form_record ( "google.com " , "1.2.3.4" )
        comp1  =  результат . разрешить ( "google.com " )
        self . assertEqual ( результат, "1.2.3.4" )

    "" "Тест: нерекурсивное разрешение имени из второй базы данных" ""
    test_resolve_2nd_dns_nonrecursive   определение ( self):
        Компьютер  =   comp1 ("Первый")
        DnsNonRecursive  =  d1 ()
        DnsNonRecursive  =  d2 ()
        d1 . set_dns ( "8.8.4.4" )
        Компьютер  =   cd1 ( "cd1")
        cd1 . get_service ( d1 )
        Компьютер  =  cd2 ( "cd2")
        cd2 . get_service ( d2 )
        d1 . set_host ( cd1 )
        d2 . set_host ( cd2)
        Сеть   =  сеть ()
        net . set_dns ( "8.8.8.8" )
        net . add_host ( comp1, "172.10.10.1" )
        comp1 . get_interface (). получить идентификаторы ()
        net . add_host ( cd1, "8.8.8.8")
        net . add_host ( cd2, "8.8.4.4")
        d2 . db . form_record ( "google.com " , "1.2.3.4" )
        comp1  =  результат . разрешить ( "google.com " )
        self . assertEqual ( результат, "1.2.3.4" )


'__main__'  ==  __name__  если :
    unittest . main ()
