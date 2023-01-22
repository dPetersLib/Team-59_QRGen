from qrgen.models import File, QrCode, QrType
from django.contrib.auth.models import User
import json
from django.http import HttpResponseRedirect
from django.urls import reverse
from QRGenProject.settings import BASE_DIR
import os
from datetime import datetime

DB_FOLDER = os.path.join(BASE_DIR, 'backups/')

# Create your views here.
def encoder(ob):
    if isinstance(ob, datetime):
        return ob.isoformat()
    return str

def backup_db(request):
    users = list(User.objects.values())
    files = list(File.objects.values())
    qrcodes = list(QrCode.objects.values())
    qrtypes = list(QrType.objects.values())

    data = [users, files, qrcodes, qrtypes]
    json_files = ['users.json', 'files.json', 'qrcodes.json', 'qrtypes.json']

    try:
        for x in data:
            for entry in x:
                entry.__delitem__('id')

        if not os.path.exists(DB_FOLDER):
            os.mkdir(DB_FOLDER)
        
        with open(os.path.join(DB_FOLDER, 'users.json'), 'w') as file:
            json.dump(users, file, default=encoder)

        with open(os.path.join(DB_FOLDER, 'files.json'), 'w') as file:
            json.dump(files, file, default=encoder) 

        with open(os.path.join(DB_FOLDER, 'qrcodes.json'), 'w') as file:
            json.dump(qrcodes, file, default=encoder)

        with open(os.path.join(DB_FOLDER, 'qrtypes.json'), 'w') as file:
            json.dump(qrtypes, file, default=encoder)
        
        for file in json_files:
            File.objects.create(
                user=request.user,
                name=f'{file}_backup',
                file=os.path.join(DB_FOLDER, file)
            )
        
        print("=" * 20)
        print("BACKUP SUCCESSFUL")
        print("=" * 20)

    except:
        print("=" * 20)
        print("BACKUP FAILED")
        print("=" * 20)

    return HttpResponseRedirect(reverse('qrgen:dashboard'))

def restore_db(request):
    if not os.path.exists(DB_FOLDER):
        # nO BACKUP FOUND
        print("=" * 20)
        print("No backup found")
        print("=" * 20)
        return HttpResponseRedirect(reverse('qrgen:dashboard'))

    with open(os.path.join(DB_FOLDER, 'users.json'), 'r') as f:
        users = json.load(f)
        db_users = User.objects.values('username')
        if len(users) > 0:
            try:
                for user in users:
                    # no duplicate username
                    if user['username'] in db_users:
                        continue
                    User.objects.create(**user)
            except:
                print("=" * 20)
                print("Error occured during restore")
                print("=" * 20)

                return HttpResponseRedirect(reverse('qrgen:dashboard'))
    with open(os.path.join(DB_FOLDER, 'files.json'), 'r') as f:
        files = json.load(f)

        if len(files) > 0:
            try:
                for file in files:
                    File.objects.create(**file)
            except:
                print("=" * 20)
                print("Error occured during restore")
                print("=" * 20)

                return HttpResponseRedirect(reverse('qrgen:dashboard'))
    with open(os.path.join(DB_FOLDER, 'qrtypes.json'), 'r') as f:
        qrtypes = json.load(f)

        if len(qrtypes) > 0:
            try:
                for qrtype in qrtypes:
                    QrType.objects.create(**qrtype)
            except:
                print("=" * 20)
                print("Error occured during restore")
                print("=" * 20)

                return HttpResponseRedirect(reverse('qrgen:dashboard'))
    with open(os.path.join(DB_FOLDER, 'qrcodes.json'), 'r') as f:
        qrcodes = json.load(f)

        if len(qrcodes) > 0:
            try:
                for qrcode in qrcodes:
                    QrCode.objects.create(**qrcode)
            except:
                print("=" * 20)
                print("Error occured during restore")
                print("=" * 20)
                return HttpResponseRedirect(reverse('qrgen:dashboard'))

    print("=" * 20)
    print("RESTORE SUCCESSFUL")
    print("=" * 20)

    return HttpResponseRedirect(reverse('qrgen:dashboard'))
