// eslint-disable-next-line
/* eslint-disable */

import Vue from 'vue'
import VueRouter from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import AdList from '@/components/AdList'
import Ads from '@/components/Ads'
import Profile from '@/components/Profile'
import Ad_detail from '@/components/Ad_detail'

Vue.use(VueRouter)

export default new VueRouter({
  routes: [
    {
      path: 'HelloWorld',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/AdList',
      name: 'AdList',
      component: AdList
    },
    {
      path: '/profile/', component: Profile,
    },
    {
      path: '/:region', component: Ads,
    },
    {
      path: '/:region/:category/', component: Ads,
    },
     {
      path: '/:region/:category/:id/', component: Ad_detail,
    }
  ]
})
