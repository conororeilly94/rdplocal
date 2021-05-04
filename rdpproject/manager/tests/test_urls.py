from django.test import SimpleTestCase
from django.urls import reverse, resolve
from manager.views import manager_list, manager_del, manager_group, manager_perms, manager_perms_del, manager_group_add, manager_group_del, users_groups, users_perms, add_users_to_groups, del_users_to_groups, manager_perms_add, users_perms_del, users_perms_add, groups_perms, groups_perms_del, groups_perms_add

class TestUrls(SimpleTestCase):

    def test_managerlist_url_is_resolves(self):
        url = reverse('manager_list')
        self.assertEquals(resolve(url).func, manager_list)

    
    def test_managerdel_url_is_resolves(self):
        url = reverse('manager_del', args=[1])
        self.assertEquals(resolve(url).func, manager_del)

    
    def test_managergroup_url_is_resolves(self):
        url = reverse('manager_group')
        self.assertEquals(resolve(url).func, manager_group)

    
    def test_managerperms_url_is_resolves(self):
        url = reverse('manager_perms')
        self.assertEquals(resolve(url).func, manager_perms)


    def test_managerpermsdel_url_is_resolves(self):
        url = reverse('manager_perms_del', args=['Paul'])
        self.assertEquals(resolve(url).func, manager_perms_del)


    def test_managergroupadd_url_is_resolves(self):
        url = reverse('manager_group_add')
        self.assertEquals(resolve(url).func, manager_group_add)


    def test_managergroupdel_url_is_resolves(self):
        url = reverse('manager_group_del', args=["Main"])
        self.assertEquals(resolve(url).func, manager_group_del)


    def test_usersgroups_url_is_resolves(self):
        url = reverse('users_groups', args=[1])
        self.assertEquals(resolve(url).func, users_groups)


    def test_usersperms_url_is_resolves(self):
        url = reverse('users_perms', args=[1])
        self.assertEquals(resolve(url).func, users_perms)


    def test_deluserstogroups_url_is_resolves(self):
        url = reverse('del_users_to_groups', args=[2, 'David'])
        self.assertEquals(resolve(url).func, del_users_to_groups)


    def test_managerpermsadd_url_is_resolves(self):
        url = reverse('manager_perms_add')
        self.assertEquals(resolve(url).func, manager_perms_add)


    def test_userspermsdel_url_is_resolves(self):
        url = reverse('users_perms_del', args=[4, 'Carl'])
        self.assertEquals(resolve(url).func, users_perms_del)


    def test_userspermsadd_url_is_resolves(self):
        url = reverse('users_perms_add', args=[1])
        self.assertEquals(resolve(url).func, users_perms_add)


    def test_groupsperms_url_is_resolves(self):
        url = reverse('groups_perms', args=['Brian'])
        self.assertEquals(resolve(url).func, groups_perms)

    
    def test_groupspermsdel_url_is_resolves(self):
        url = reverse('groups_perms_del', args=['Louise', 'Phil'])
        self.assertEquals(resolve(url).func, groups_perms_del)


    def test_groupspermsadd_url_is_resolves(self):
        url = reverse('groups_perms_add', args=['Derek'])
        self.assertEquals(resolve(url).func, groups_perms_add)