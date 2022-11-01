из   общего   импорта   *
импорт   единицы измерения

Класс   тестового компьютера ( unittest . Тестовый пример ):
    "" "Тест: адрес компьютера" ""
    определение   test_ip (self):
        Компьютер  =   comp ("Первый")
        Сеть   =  сеть ()
        net . add_host ( комп, "172.10.10.1")
        comp  =  результат . get_interface (). адрес
        self . assertEqual ( результат, "172.10.10.1" )

    "" "Тест: имя компьютера" ""
    определение   имя_теста ( self ):
        Компьютер  =   comp ("Первый")
        Сеть   =  сеть ()
        net . add_host ( комп, "172.10.10.1")
        result  =  comp . name
        self . assertEqual ( result , "First" )

    "" "Test: ping without network" ""
    def  test_ping_without_net ( self ):
        comp  =  Computer ( "First" )
        result  =  comp . ping ( "172.10.10.10" )
        self . assertEqual ( result , "No network" )

    "" "Test: ping" ""
    def  test_ping ( self ):
        comp1  =  Computer ( "First" )
        Компьютер  =  comp2 ( "Второй" )
        Сеть   =  сеть ()
        net . add_host ( comp1, "172.10.10.1" )
        net . add_host ( comp2, "172.10.10.2" )
        comp1  =  результат . проверка ( "172.10.10.2")
        self . assertEqual ( результат: "Успешный пинг с 172.10.10.1 по 172.10.10.2" )

    "" "Тест: получить имя компьютера" ""
    comp_get_name   определение ( self ):
        Компьютер  =   comp ("Первый")
        Сеть   =  сеть ()
        addr  =  "1.2.3.4"
        net . add_host ( comp , addr)
        чистый  =  результат . hosts [ addr ]. get_name ()
        self . assertEqual (результат, "Первый" )

    "" "Тест: разрешение имени несуществующего компьютера" ""
    test_comp_resolve_unk_name   определение ( self ):
        Компьютер  =   comp ("Первый")
        Сеть   =  сеть ()
        net . add_host ( комп, "172.10.10.1")
        comp  =  результат . local_resolve ( "172.10.10.2" )
        self . assertEqual ( результат, "Неизвестный хост" )

    "" "Тест: разрешить имя компьютера" ""
    test_comp_name_resolve   определение ( self ):
        Компьютер  =   comp1 ("Первый")
        Компьютер  =  comp2 ( "Второй" )
        Сеть   =  сеть ()
        net . add_host ( comp1, "172.10.10.1" )
        net . add_host ( comp2, "172.10.10.2" )
        comp1  =  результат . local_resolve ( "172.10.10.2" )
        self . assertEqual (результат, "Второй" )

Класс   TestNetworkInterface ( unittest . Тестовый пример ):
    "" "Тест: адрес компьютера" ""
    определение   test_set_net ( self ):
        Компьютер  =   comp ("Первый")
        net  =  Network ()
        address  =  "1.2.3.4"
        comp . get_interface (). setNet ( net , address )
        result  =  comp . get_interface (). address
        self . assertEqual ( result , "1.2.3.4" )

    "" "Test: install DNS server" ""
    def  test_set_dns ( self ):
        comp  =  Computer ( "First" )
        address  =  "8.8.8.8"
        comp . get_interface (). setDns ( address )
        result  =  comp . get_interface (). dns
        self . assertEqual ( result , "8.8.8.8" )

    "" "Test: disconnect from the network" ""
    def  test_disconnect ( self ):
        comp  =  Computer ( "First" )
        net  =  Network ()
        net . add_host ( comp , "172.10.10.1" )
        comp . get_interface (). disconnect ()
        result  =  comp . get_interface (). address
        self . assertEqual ( result , None )
        result  =  comp . get_interface (). net
        self . assertEqual ( result , None )

    "" "Test: getting DNS from a network without a network" ""
    def  test_get_dns_without_net ( self ):
        Компьютер  =   comp ("Первый")
        comp  =  результат . get_interface (). get_dns ()
        self . assertEqual ( результат: "Нет сети" )

    "" "Тест: получение " пустого " DNS из сети" ""
    test_get_empty_dns   определение (self):
        Компьютер  =   comp ("Первый")
        Сеть   =  сеть ()
        net . add_host ( комп, "172.10.10.1")
        comp . get_interface (). get_dns ()
        comp  =  результат . get_interface (). dns
        self . assertEqual ( результат, "Нет DNS" )

    "" "Тест: получение DNS из сети" ""
    test_get_dns   определение (self):
        Компьютер  =   comp ("Первый")
        Сеть   =  сеть ()
        net . add_host ( комп, "172.10.10.1")
        net . set_dns ( "8.8.8.8" )
        comp . get_interface (). get_dns ()
        comp  =  результат . get_interface (). dns
        self . assertEqual ( результат, "8.8.8.8" )

Тестовый   сетевой класс (unittest . Тестовый пример ):
    "" "Тест: количество хостов в сети" ""
    test_hosts_num   определение (self):
        Компьютер  =   comp1 ("Первый")
        Компьютер  =  comp2 ( "Второй" )
        Сеть   =  сеть ()
        net . add_host ( comp1, "172.10.10.1" )
        net . add_host ( comp2, "172.10.10.2")
        net  =  результат . get_hosts_num ()
        self . assertEqual ( результат, 2 )
        Компьютер  =   comp3 ( "Третий")
        net . add_host ( comp3, "172.10.10.3")
        net  =  результат . get_hosts_num ()
        self . assertEqual ( результат, 3 )

    "" "Test: add a computer with a busy address" ""
    def  test_busy_address ( self ):
        comp1  =  Computer ( "First" )
        comp2  =  Computer ( "Second" )
        net  =  Network ()
        net . add_host ( comp1 , "172.10.10.1" )
        result  =  net . add_host ( comp2 , "172.10.10.1" )
        self . assertEqual ( result , "Busy address" )

    "" "Test: re-add a computer with a different address" ""
    def  test_rewrite_address ( self ):
        comp  =  Computer ( "First" )
        net  =  Network ()
        net . add_host ( comp , "172.10.10.1" )
        net . add_host ( comp , "172.10.10.2" )
        result  =  comp . get_interface (). address
        self . assertEqual ( result , "172.10.10.2" )
        result  =  net . get_hosts_num ()
        self . assertEqual ( result , 1 )

    "" "Test: resolving the name of a non-existent computer" ""
    def  test_resolve_unk_host ( self ):
        Сеть   =  сеть ()
        адрес  =  "1.2.3.4"
        net  =  результат . net_resolve (адрес )
        self . assertEqual ( результат, "Неизвестный хост" )

    "" "Тест: разрешить имя компьютера" ""
    определение   test_resolve_host (self):
        Компьютер  =   comp ("Первый")
        Сеть   =  сеть ()
        net . add_host ( комп, "172.10.10.1")
        net  =  результат . net_resolve ( comp . get_interface (). address )
        self . assertEqual (результат, "Первый" )

    "" "Тест: разрешить имя компьютера в сети" ""
    test_local_resolve   определение ( self):
        Компьютер  =   comp1 ("Первый")
        Компьютер   =   comp2 ("Второй")
        Сеть   =  сеть ()
        net . add_host ( comp1, "172.10.10.1" )
        net . add_host ( comp2, "172.10.10.2")
        comp1  =  результат . get_interface (). local_resolve ( "172.10.10.2")
        self . assertEqual (результат, "Второй" )

    "" "Тест: Отправить сообщение" ""
    test_send_msg   определение ( self ):
        Компьютер  =   comp1 ("Первый")
        Компьютер   =   comp2 ("Второй")
        Сеть   =  сеть ()
        net . add_host ( comp1, "172.10.10.1" )
        net . add_host ( comp2, "172.10.10.2")
        comp1 . form_msg ( "172.10.10.2", "ICQ", "OLOLO")
        comp2  =  результат . all_data [ len ( comp2 . all_data ) - 1 ]. get_data ()
        self . assertEqual ( результат , "OLOLO" )

    "" "Тест: получение отправленного сообщения после подключения" ""
    test_get_msg_after_connect   определение ( self ):
        Компьютер  =   comp1 ("Первый")
        Сеть   =  сеть ()
        net . add_host ( comp1, "172.10.10.1" )
        comp1 . form_msg ( "172.10.10.2", "ICQ", "abcde")
        net  =  результат . num_msgs ()
        self . assertEqual ( результат, 1 )
        Компьютер   =   comp2 ("Второй")
        net . add_host ( comp2, "172.10.10.2")
        net  =  результат . num_msgs ()
        self . assertEqual ( результат, 0 )
        comp2  =  результат . all_data [ len ( comp2 . all_data ) - 1 ]. get_data ()
        self . assertEqual ( результат, "abcde" )

    "" "Тест: запрос сообщения из пустой очереди" ""
    test_no_messages   определение (self):
        Компьютер  =   comp1 ("Первый")
        Сеть   =  сеть ()
        net . add_host ( comp1, "172.10.10.1" )
        comp1  =  результат . find_msg ()
        self . assertEqual ( результат, "Нет сообщений" )

'__main__'  ==  __name__  если :
    unittest . main ()
