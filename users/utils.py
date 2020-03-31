from app.models import StarUser


def get_user_data(user):
    user_info = dict()
    user_info['id'] = user.id
    user_info['email'] = user.email
    user_info['first_name'] = user.first_name
    user_info['last_name'] = user.last_name
    user_info['is_active'] = user.is_active
    user_info['is_staff'] = user.is_staff
    user_info['date_joined'] = user.date_joined
    user_info['vote_ids'] = [
        star.star_id.id for star in StarUser.objects.filter(user_id=user.id)
    ]
    return user_info
