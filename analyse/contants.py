import os

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROCESSED_DIR = os.path.join(PROJECT_DIR, "processed")
RAW_DATA_DIR = os.path.join(PROJECT_DIR, "raw data")
BBOXES_WITH_TAGS_DIR = os.path.join(PROCESSED_DIR, "bboxes_with_tags")
LINES_DATA_DIR = os.path.join(PROCESSED_DIR, "lines_data_text_files")
RESULTS_DIR = os.path.join(PROJECT_DIR, 'results')
TEMP_DIR = os.path.join(PROJECT_DIR, 'temp')
LINES_WITH_ID_IMAGES = os.path.join(PROCESSED_DIR, "lines_with_id_images")
LINES_DRAWN_IMAGES = os.path.join(PROCESSED_DIR, "lines_drawn_images")
BLACK_WHITE = os.path.join(PROCESSED_DIR, "black_white")

dateRegExp_ = [
        "\d{2}[-/]\d{2}[-/]\d{4}", '\d{1}[-/]\d{2}[-/]\d{4}', '\d{1}[-/]\d{1}[-/]\d{4}',
        '\d{1}[-/]\d{1}[-/]\d{4}', '\d{1}[-/]\d{1}[-/]\d{3}', '\d{4}[-/]\d{2}[-/]\d{2}',
        '\d{2}[-/]\d{2}[-/]\d{2}','\d{4}[-/:]\d{2}[-/:]\d{2}','\d{2}[-/:]\d{2}[-/:]\d{2}'
        '\d{2}[-/]\w{3}[-/]\d{2}', '\d{2}[-/]\w{3}[-/]\d{4}', '\d{4}[-/]\w{3}[-/]\d{2}',
        '\w{3}\s\d{2}[,]\s\d{4}', '\w{3}\s\d{2}[.]\s\d{4}', '\w{3}\s\d{2}[,]\s\d+',
        '\w{3}\s\d{2}[.]\s\d+', '\w+\s\d{2}[.]\d{4}', '\w+\s\d{2}[,]\d{4}', '\w+\s\d{2}[,]\s\d{4}',
        '\w+\s\d{2}[.]\s\d{4}', '\d{1}[-/]\d{1}\s\d{1}[-/]\d{4}', '\w+\s\d{2}[.]\s\d{4}',
        '\w+\s\d{2}[.]\s\w{4}', '\w+\s\d{2}[.]\s\d{4}', '\w+\s\d+[,]\s\d+', '\w+\s\d+[.]\s\d+',
        '([a-zA-Z0-9]{3,9}[-/.,\\s]{1,3}[a-zA-Z0-9]{1,3}[-/.,\\s]{1,2}[a-zA-Z0-9]{2,4})',
              ]

InvDateKey_ = [
        'invoice date', 'lnvoice date', 'inv0ice date', 'involce date', 'lnvolce date', 'lv0lce date',
        'date', 'dte', 'inv dte', 'invoice dte',
        'inv date', 'inice date', 'invice date', 'vice date', 'vice dte', 'vce date', 'vce dte',
        'voice date', 'vice date',
        'ce date', 'iv0lce date', 'nv0lce date', 'iv0lce date', '0lce date', 'nvice date', 'da',
        'in da',
        'inv da','nvolce date','invoice date', 'issue date', 'due date', 'shipping date']

invoice_number_list_ = [
        'Account Invoice Number', '_ Payaa__Referange/Invoice_No', 'Payne Refnrenca/Invonca No',
        'Payn Rlinrencn/Invoice No', 'Accountl Invoice Number', 'Payee I_2_I_1gronco/Invoico No',
        'Account/Invoice Number', 'Invo ca Number', 'IN/QIVCE NUM_BER', 'VNVOICE NUMBER',
        '|NvocE NUMBER', 'Invoice NO.', 'Invoice N0.', 'Invoice Number:',
        'Payne Refnrenca/Invonca No',
        'Payee Relarence/I nvoice No', 'Invo ca Number', 'Involco Numbor', 'lnvolca Number',
        'INVOICE .LMl-ID', 'I Invoice Number', 'Invoice No', 'INVOICE NO.', 'invoice Number',
        'INVOICE NO,', 'INVOICE ID', 'invoice Number', 'voice number', 'volce number', 'v0lce number',
        'InvoiceNumber', 'Invnice Number', 'Invoice Number', 'InvNo', 'Inv. No.', 'ivol Number',
        'InvoiceNo', 'IHVODCE No', 'lvoice Number', 'lvolce Number', 'l_lnoice Number', 'Invoice It',
        'Invoice #', 'invoice', 'lvoice', 'lnvo ce Number', 'INVOICE NUMBER', 'IIQVOICE NUMBER',
        'Invoice No.', 'invoice No.', 'Invoice Number', 'lnvolco Number', 'invoice n0', 'inv0ice n0',
        'inv0ice no' 'lnvqige Number', 'lnv0ice Number', 'Invoice ilumbef', '1nvoice Number',
        '1ce Number', 'nvoice Number', 'lnvolceNo', 'lnvolce No.', 'lnvolceNumber', 'Vendor Invoice',
        'I lNV0lIl- NO', 'WVO. C5. NUMBER', 'INV',
        'lnvolce Number', 'noviceNo', 'v0ice Number', 'Booking Reference', 'Involce Number',
        'lvolce',
        'lv0lce', 'nvo ca Number', 'Quo No.', 'Invoke: No', 'nvoice Number', 'mvouce NUMBER',
        'COMM|.N|',
        'COMMENT', 'COMMENT', 'Reference', 'DESCRIPTION', 'VOUCHER NO.'
                      ]

amount_list_ = [
        'Net Pnld Amt', 'Net Paid Amt', 'Net Invoice Amount', 'Invoice Net Amt', 'NET AMOUNT',
        'Palmenl Amount', 'AMOUNT PAID', 'Invoice Amt', 'Paid Amount', 'NET AMOUNT', 'ET AMOUNT',
        'Net Amount', 'Payment Amount', 'Praymenti Amounl', 'NVO CI AMOJNI', 'G ROSS AMOUNT',
        'GROSS AMOUNT', 'AHOUN I PA I I', 'Amou nt', 'Amount', 'AMOUNT', 'Amt', 'MOUNT', 'Amognt',
        'NET',
        'ff/OIICB Am', 'Payment','1voice amount', '1nvoice amount', '1nvo1ce amount', 'invoice amt',
        '1nvoice amt',
        '1nvo1ce amt',
        'invo1ce amt', 'inv0ice amt', '1nv01ce amt','inv0ice amount', '1nv01ce amount',
        'inv0ice amount',
        'voce amount', 'gross amount', 'Gr0os amnt',
        'gr00s am0unt', 'gross amnt', 'groamnt', 'vo1ce amount', 'vo1ce amt', 'ce amt', 'ce amount',
        'in amount', 'in amt', 'paid', 'pald',
        'in amnt', 'v0 amnt', 'v0 amount', 'pavment', 'payment', 'v0 am0unt', '1n am0unt', 'ce amnt',
        'ce amount', 'ce am0unt', 'ce amt', 'ic amount', 'ic amnt', 'ic am0unt', 'ic amnt', 'gfoos',
        'not',
        'pa1d amnt',
        'pa1d am0unt', 'net am0unt', 'et amnt', 'et amt', 'am0unt', 'amunt', 'amount paid',
        'am0unt paid',
        'amun paid', 'etunt', 'netunt', 'not am0unt', 'not amount', 'Due', 'Total'
                ]

amountRegExp_ = [
        '\d+[,]\d+[.]\d{2}', '\d+[,]\d+[_]\d{2}', '\d+[,]\d+[.]\d+\s+\d+', '\d+[,]\d+[_]\d+\s+\d+',
        '\d+[.]\d+\s+\d+', '\d+[_]\d+', '\d+[.]\d+', '\d+[.]\d{2}', '\d+[_]\d{2}', '\d+\s{1}\d{2}',
        '\d+\w+[_]\d{1}\w{1}', '\d+\w+[.]\d{2}', '\d+\w+[.]\d{1}\w{1}', '\d+\w+[_]\w{1}\d{1}',
        '\d+\w+[.]\w{1}\d{1}', '\d+\w+[.]\s{1}\d{2}', '\d+[a-zA-Z]\d{1}', '\d+[,]\d+', '\d+[,]\s\d+',
        '\d[2]+'
                ]

addresses_list_ = [
                "Billing Address", "Shipping Address", "Bill to", "Ship to",
                "Accounts Receivable", "Billed to", "Shipped to", "Invoiced to",
                "From", "To", "Consigner", "Sold to", "Address", "Shipped"
                  ]
