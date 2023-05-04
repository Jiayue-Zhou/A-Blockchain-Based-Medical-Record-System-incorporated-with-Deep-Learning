import Vue from 'vue';
import VueRouter from 'vue-router';
// import Doctor from '../views/Doctor.vue';
// import newDoctor from '../views/newDoctor.vue';
import Doctor from '../views/Doctor.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Doctor',
    component: Doctor,
  },
  {
    path: '/patient',
    name: 'Patient',
    // component: Patient
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/Patient.vue'),
  },
  {
    path: '/doctor',
    name: 'Doctor',
    // component: Patient
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/Doctor.vue'),
  },
  {
    path: '/newDoctor',
    name: 'newDoctor',
    // component: Patient
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/newDoctor.vue'),
  },
];

const router = new VueRouter({
  routes,
});

export default router;
