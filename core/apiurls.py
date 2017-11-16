"""API URL Configuration"""

from django.conf.urls import url

from . import api

urlpatterns = [
    url(
        r'^check_duplication/$',
        api.check_duplication,
        name='check_duplication'
    ),
    url(
        r'^get_verification_code/$',
        api.get_verification_code,
        name='get_verification_code',
    ),
    url(
        r'^check_validation/$',
        api.check_validation,
        name='check_validation'
    ),
    url(
        r'^like_article/$',
        api.like_article,
        name='like_article',
        kwargs={'liketype': 'like'}
    ),
    url(
        r'^dislike_article/$',
        api.like_article,
        name='dislike_article',
        kwargs={'liketype': 'dislike'}
    ),
    url(
        r'^like_users/$',
        api.like_users,
        name='like_users',
        kwargs={'liketype': 'like'}
    ),
    url(
        r'^dislike_users/$',
        api.like_users,
        name='dislike_users',
        kwargs={'liketype': 'dislike'}
    ),
    url(
        r'^like_reply/$',
        api.like_reply,
        name='like_reply',
        kwargs={'liketype': 'like'}
    ),
    url(
        r'^dislike_reply/$',
        api.like_reply,
        name='dislike_reply',
        kwargs={'liketype': 'dislike'}
    ),
    url(
        r'^write_reply/$',
        api.write_reply,
        name='write_reply',
    ),
    url(
        r'^reload_reply/$',
        api.reload_reply,
        name='reload_reply',
    ),
    url(
        r'^delete_reply/$',
        api.delete_reply,
        name='delete_reply',
    ),
    url(
        r'^restore_reply/$',
        api.restore_reply,
        name='restore_reply',
    ),
    url(
        r'^reply_count/$',
        api.reply_count,
        name='reply_count',
    ),
    url(
        r'^toggle_bookmark/$',
        api.toggle_bookmark,
        name='toggle_bookmark',
    ),
    url(
        r'^edit_bookmarks/$',
        api.edit_bookmarks,
        name='edit_bookmarks',
    ),
    url(
        r'^scrap/$',
        api.scrap,
        name='scrap',
    ),
    url(
        r'^alarm_status/$',
        api.alarm_status,
        name='alarm_status'
    ),
    url(
        r'^alarm_list/$',
        api.alarm_list,
        name='alarm_list'
    ),
    url(
        r'^clear_alarm/$',
        api.clear_alarm,
        name='clear_alarm'
    ),
    url(
        r'^delete_message/$',
        api.delete_message,
        name='delete_message'
    ),
    url(
        r'^write_team_reply/$',
        api.write_team_reply,
        name='write_team_reply',
    ),
    url(
        r'^reload_team_reply/$',
        api.reload_team_reply,
        name='reload_team_reply',
    ),
    url(
        r'^delete_team_reply/$',
        api.delete_team_reply,
        name='delete_team_reply',
    ),
    url(
        r'^restore_team_reply/$',
        api.restore_team_reply,
        name='restore_team_reply',
    ),
    url(
        r'^team_reply_count/$',
        api.team_reply_count,
        name='team_reply_count',
    ),
    url(
        r'^join_team/$',
        api.join_team,
        name='join_team'
    ),
    url(
        r'^leave_team/$',
        api.leave_team,
        name='leave_team'
    ),
    url(
        r'^kick_player/$',
        api.kick_player,
        name='kick_player'
    ),
    url(
        r'^reload_team/$',
        api.reload_team,
        name='reload_team'
    ),
    url(
        r'^like_post/$',
        api.like_post,
        name='like_post',
    ),
    url(
        r'^write_comment/$',
        api.write_comment,
        name='write_comment',
    ),
    url(
        r'^delete_comment/$',
        api.delete_comment,
        name='delete_comment',
    ),
    url(
        r'^reload_comment/$',
        api.reload_comment,
        name='reload_comment',
    ),
]
