sed -i 's/g_build_filename (\(.\+\), NULL);/g_build_filename (\1, (gchar *)NULL);/' /gnucash-3.3/libgnucash/core-utils/gnc-filepath-utils.cpp /gnucash-3.3/libgnucash/engine/qof-backend.cpp

sed -e 's/g_strconcat (\(.\+\), NULL);/g_strconcat (\1, (gchar *)NULL);/' -e 's/g_strconcat (\(.\+\), NULL );/g_strconcat (\1, (gchar *)NULL);/' -i /gnucash-3.3/libgnucash/backend/xml/sixtp-utils.cpp /gnucash-3.3/libgnucash/engine/qofbook.cpp /gnucash-3.3/libgnucash/engine/qoflog.cpp /gnucash-3.3/libgnucash/engine/Account.cpp /gnucash-3.3/libgnucash/engine/qoflog.cpp

sed -i 's/fname = g_strconcat(log_filename, ".XXXXXX.log", NULL);/fname = g_strconcat(log_filename, ".XXXXXX.log", (gchar *)NULL);/' /gnucash-3.3/libgnucash/engine/qoflog.cpp

sed -i 's/g_object_get (\(.\+\), NULL);/g_object_get (\1, (gchar *)NULL);/' /gnucash-3.3/libgnucash/backend/sql/gnc-sql-column-table-entry.cpp /gnucash-3.3/libgnucash/backend/sql/gnc-schedxaction-sql.cpp /gnucash-3.3/gnucash/gnome/assistant-loan.cpp

sed -i 's/             NULL);/             (gchar *)NULL);/' /gnucash-3.3/gnucash/gnome/assistant-loan.cpp

sed -i 's/gnc_commodity_get_mnemonic (currency), NULL);/gnc_commodity_get_mnemonic (currency), (gchar *)NULL);/' /gnucash-3.3/libgnucash/engine/Account.cpp

sed -i 's/g_object_set (\(.\+\), NULL);/g_object_set (\1, (gchar *)NULL);/' /gnucash-3.3/gnucash/gnome/assistant-loan.cpp