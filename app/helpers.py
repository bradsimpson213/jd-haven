from csv import DictReader, DictWriter
from .models import db, Record, LastUpdate
from datetime import datetime 

def convert_file_to_dict(file):
    """converts the csv file to a python list of dictionaries"""
    
    with open('tempdata.csv', 'wb+') as destination:
        for chunk in file:
            destination.write(chunk)
    
    with open('tempdata.csv') as file:
        csv_reader = DictReader(file)
        data = list(csv_reader)
        filtered = [record for record in data if record["policyNumber"] != ""]
        print("This many records without policy numbers were removed:", len(data) - len(filtered))
        return filtered


def save_records(records, save_date):
    """turns the list of records into record rows in the db"""
    count = 0
    date_format = "%Y-%m-%d %H:%M:%S"
    default_date = None
    current_policies = [record.policyNumber for record in Record.query.all()]

    for record in records:
        if record['policyNumber'] in current_policies:
            continue

        new_record= Record(
            created_on = save_date,
            customer_id = record['customer_id'],
            policyNumber = record['policyNumber'],
            referralId = record['referralId'],
            accountCreateDate = datetime.strptime(record['accountCreateDate'],date_format) if record['accountCreateDate'] else default_date,
            igoDate = datetime.strptime(record['igoDate'],date_format) if record['igoDate'] else default_date,
            offerDate = datetime.strptime(record['offerDate'], date_format) if record['offerDate'] else default_date,
            applicationSignedDate = datetime.strptime(record['applicationSignedDate'], date_format) if record['applicationSignedDate'] else default_date,
            issuedDate = datetime.strptime(record['issuedDate'], date_format) if record['issuedDate'] else default_date,
            status = record['status'],
            paidToDate = datetime.strptime(record['paidToDate'], date_format) if record['paidToDate'] else default_date,
            canceled_ir = record['canceled_ir'],
            declined_ir = record['declined_ir'],
            monthlyPremium = record['monthlyPremium'],
            faceAmount = record['faceAmount'],
            term = record['term'],
            finalRateClass = record['finalRateClass'],
            finalRateClassName = record['finalRateClassName'],
            paidSource = record['paidSource'],
            paidSource_campaign = record['paidSource_campaign'],
            telesalesAgency = record['telesalesAgency'],
            agentName = record['agentName'],
            product = record['product'],
            initialProductType = record['initialProductType'],
            firstName = record['firstName'],
            lastName = record['lastName'],
            dateOfBirth = datetime.strptime(record['dateOfBirth'], date_format) if record['dateOfBirth'] else default_date,
            email = record['email'],
            address = record['address'],
            phoneNumber = record['phoneNumber'],
        )
     
        db.session.add(new_record)
        db.session.commit()
        count += 1

    print(f"{count} records were created!")
    updated = LastUpdate(last_update=save_date)
    db.session.add(updated)
    db.session.commit()
    return True