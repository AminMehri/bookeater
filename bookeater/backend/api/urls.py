from django.urls import path, include
from . import views

urlpatterns = [
    path('ShowAllNews/', views.ShowAllNews.as_view(), name="show_all_news"),
    path('ShowQuotes/', views.ShowQuotes.as_view(), name="show_quotes"),
    path('ShowBestBooks/', views.ShowBestBooks.as_view(), name="show_best_books"),
    path('ShowPopularCategories/', views.ShowPopularCategories.as_view(), name="show_popular_categories"),
    path('ShowMostRatedBooks/', views.ShowMostRatedBooks.as_view(), name="show_most_rated_books"),
    path('ShowPopularAuthors/', views.ShowPopularAuthors.as_view(), name="show_popular_authors"),
    path('ShowAllCategories/', views.ShowAllCategories.as_view(), name="show_all_categories"),
    path('ShowAllAuthors/', views.ShowAllAuthors.as_view(), name="show_all_authors"),
    path('ShowAllReviewedBooks/', views.ShowAllReviewedBooks.as_view(), name="show_allreviewed_books"),
    path('ShowSingleNews/', views.ShowSingleNews.as_view(), name="show_single_news"),
    path('ShowSingleBook/', views.ShowSingleBook.as_view(), name="show_single_book"),
    path('ShowSingleCategory/', views.ShowSingleCategory.as_view(), name="show_single_category"),
    path('ShowSingleAuthor/', views.ShowSingleAuthor.as_view(), name="show_single_author"),
    path('ShowSingleReviewedBook/', views.ShowSingleReviewedBook.as_view(), name="show_single_reviewed_book"),
    path('ShowProfile/', views.ShowProfile.as_view(), name="show_profile"),
    path('UpdateProfileInformation/', views.UpdateProfileInformation.as_view(), name="update_profile_information"),
    path('ShowReadList/', views.ShowReadList.as_view(), name="show_read_list"),
    path('ContactUs/', views.ContactUs.as_view(), name="contact_us"),
    path('MakeRate/', views.MakeRate.as_view(), name="make_rate"),
    path('AddOrRemoveFromReadlist/', views.AddOrRemoveFromReadlist.as_view(), name="add_or_remove_from_read_list"),
    path('MakeComment/', views.MakeComment.as_view(), name="make_comment"),
    path('ShowComment/', views.ShowComment.as_view(), name="show_comment"),
    path('LikeComment/', views.LikeComment.as_view(), name="like_comment"),
    path('DisLikeComment/', views.DisLikeComment.as_view(), name="dis_like_comment"),
    path('ShowUserComment/', views.ShowUserComment.as_view(), name="show_user_comment"),
    path('SendEmail/', views.SendEmail.as_view(), name="send_email"),
    path('VerifyEmail/', views.VerifyEmail.as_view(), name="verify_email"),

    # author panel urls
    path('ShowBooksPanel/', views.ShowBooksPanel.as_view(), name="show_books_panel"),
    path('ShowNewsPanel/', views.ShowNewsPanel.as_view(), name="show_news_panel"),
    path('ShowQuotesPanel/', views.ShowQuotesPanel.as_view(), name="show_quotes_panel"),
    path('ShowCategoriesPanel/', views.ShowCategoriesPanel.as_view(), name="show_categories_panel"),
    path('ShowAuthorsPanel/', views.ShowAuthorsPanel.as_view(), name="show_authors_panel"),
    path('ShowReviewedBooksPanel/', views.ShowReviewedBooksPanel.as_view(), name="show_reviewed_books_panel"),
    path('AddBookPanel/', views.AddBookPanel.as_view(), name="add_book_panel"),
    
]
