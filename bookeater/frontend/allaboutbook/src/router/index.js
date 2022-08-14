import { createRouter, createWebHistory } from 'vue-router'
import store from '../store'

import Home                      from '../views/Home.vue'
import Readlist                  from '../views/Readlist.vue'
import Login                     from '../views/Login.vue'
import Register                  from '../views/Register.vue'
import All_Categories            from '../views/All_Categories.vue'
import All_Authors               from '../views/All_Authors.vue'
import Single_Category           from '../views/Single_Category.vue'
import Single_Author             from '../views/Single_Author.vue'
import Reviewed_Books            from '../views/All_Reviewed_Books.vue'
import Single_Reviewed_Books     from '../views/Single_Reviewed_Books.vue'
import News                      from '../views/All_News.vue'
import Best_Books                from '../views/Best_Books.vue'
import Most_Rated_Books          from '../views/Most_Rated_Books.vue'
import Path_Not_Found            from '../views/Path_Not_Found.vue'
import Book_Detail               from '../views/Book_Detail.vue'
import Single_News               from '../views/Single_News.vue'
import Profile                   from '../views/Profile.vue'
import User                      from '../views/User.vue'
import Password_Reset_Confirm    from '../views/Password_Reset_Confirm.vue'
import ContactUs                 from '../views/ContactUs.vue'
import AboutUs                   from '../views/AboutUs.vue'
import Developers                from '../views/Developers.vue'
import EmailVerify               from '../views/EmailVerify.vue'

// author panel views
import Author_Panel              from '../views/Author-panel/Author_Panel.vue'
import Books                     from '../views/Author-panel/Books.vue'
import Add_Book                  from '../views/Author-panel/Add_Book.vue'
import Categories                from '../views/Author-panel/Categories.vue'
import Add_Category              from '../views/Author-panel/Add_Category.vue'
import Authors                   from '../views/Author-panel/Authors.vue'
import Add_Author                from '../views/Author-panel/Add_Author.vue'
import Reviewed_Books_Panel      from '../views/Author-panel/Reviewed_Books.vue'
import Add_Reviewed_Book         from '../views/Author-panel/Add_Reviewed_Book.vue'
import Quotes                    from '../views/Author-panel/Quotes.vue'
import Add_Quote                 from '../views/Author-panel/Add_Quote.vue'
import News_Panel                      from '../views/Author-panel/News.vue'
import Add_News                  from '../views/Author-panel/Add_News.vue'
// author panel views

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/readlist',
    name: 'readlist',
    component: Readlist
  },
  {
    path: '/login',
    name: 'login',
    component: Login,
    meta: { loginRedirect: true }
  },
  {
    path: '/register',
    name: 'register',
    component: Register,
    meta: { loginRedirect: true }
  },
  {
    path: '/categories',
    name: 'all_categories',
    component: All_Categories
  },
  {
    path: '/authors',
    name: 'all_authors',
    component: All_Authors
  },
  {
    path: '/category/:slug',
    name: 'single_category',
    component: Single_Category
  },
  {
    path: '/author/:slug',
    name: 'single_author',
    component: Single_Author
  },
  {
    path: '/reviewed-books',
    name: 'reviewed_books',
    component: Reviewed_Books
  },
  {
    path: '/reviewed-book/:slug',
    name: 'single_reviewed_books',
    component: Single_Reviewed_Books
  },
  {
    path: '/news',
    name: 'news',
    component: News
  },
  {
    path: '/news/:slug',
    name: 'single_news',
    component: Single_News
  },
  {
    path: '/best-books',
    name: 'best_books',
    component: Best_Books
  },
  {
    path: '/most-rated-books',
    name: 'most_rated_books',
    component: Most_Rated_Books
  },
  {
    path: '/book/:slug',
    name: 'book_detail',
    component: Book_Detail
  },
  {
    path: '/profile',
    name: 'profile',
    component: Profile,
  },
  {
    path: '/user/:username',
    name: 'user',
    component: User,
  },
  {
    path: '/contact-us',
    name: 'contact-us',
    component: ContactUs,
  },
  {
    path: '/about-us',
    name: 'about-us',
    component: AboutUs,
  },
  {
    path: '/developers',
    name: 'developers',
    component: Developers,
  },
  // author panel
  {
    path: '/author-panel',
    name: 'author-panel',
    component: Author_Panel,
  },
  {
    path: '/author-panel/books',
    name: 'author-panel-books',
    component: Books,
  },
  {
    path: '/author-panel/add-book',
    name: 'author-panel-add-book',
    component: Add_Book,
  },
  {
    path: '/author-panel/categories',
    name: 'author-panel-categories',
    component: Categories,
  },
  {
    path: '/author-panel/add-category',
    name: 'author-panel-add-category',
    component: Add_Category,
  },
  {
    path: '/author-panel/authors',
    name: 'author-panel-authors',
    component: Authors,
  },
  {
    path: '/author-panel/add-author',
    name: 'author-panel-add-author',
    component: Add_Author,
  },
  {
    path: '/author-panel/reviewed-books',
    name: 'author-panel-reviewed-books',
    component: Reviewed_Books_Panel,
  },
  {
    path: '/author-panel/add-reviewed-book',
    name: 'author-panel-add-reviewed-book',
    component: Add_Reviewed_Book,
  },
  {
    path: '/author-panel/news',
    name: 'author-panel-news',
    component: News_Panel,
  },
  {
    path: '/author-panel/add-news',
    name: 'author-panel-add-news',
    component: Add_News,
  },
  {
    path: '/author-panel/quotes',
    name: 'author-panel-quotes',
    component: Quotes,
  },
  {
    path: '/author-panel/add-quote',
    name: 'author-panel-add-quote',
    component: Add_Quote,
  },
  // end author panel
  {
    path: '/email-verify/:token',
    name: 'email-verify',
    component: EmailVerify,
  },
  {
    path: '/dj-rest-auth/password/reset/confirm/:uid/:token',
    name: 'password_reset_confirm',
    component: Password_Reset_Confirm,
    meta: { loginRedirect: true }
  },
  {
    path: '/:pathMatch(.*)*', 
    name: 'not_found',
    component: Path_Not_Found
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})


router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.loginRequired)) {
    if (store.state.isAuthenticated) {
      next()
    } else {
      next("/login")
    }
  }else if (to.matched.some(record => record.meta.loginRedirect)) {
    if (store.state.isAuthenticated) {
      next("/profile")
    } else {
      next()
    }
  } else {
    next()
  }
})

export default router
