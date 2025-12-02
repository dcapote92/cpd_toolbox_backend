from django.contrib.auth.models import BaseUserManager

class CustomManager(BaseUserManager):
    """_summary_
        Custom user manager to use GM-ID as identifier 
    """

    def create_user(self, gm_id, password=None, **extra_fields):
        if not gm_id:
            raise ValueError('O GM-ID deve ser fornecido')
        
        user = self.model(gm_id=gm_id, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, gm_id, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser deve ter is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser deve ter is_superuser=True.')
        
        return self.create_superuser(gm_id, password, **extra_fields)