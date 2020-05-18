from datetime import datetime

def write_line_log(directory, text):
    date_time = datetime.now()
    current_date = date_time.strftime('%H:%M:%S - %d/%m/%Y')
    daily_log_filename = date_time.strftime('%Y_%m_%d_log.log')

    log_text = f'{current_date} {text} \n'

    full_log = open(directory + '/' + 'full_log.log', 'a+')
    full_log.write(log_text)
    full_log.close()

    daily_log = open(directory + '/' + daily_log_filename, 'a+')
    daily_log.write(log_text)
    daily_log.close()

