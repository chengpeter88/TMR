
# %% [markdown]
# ## 引入套件
from util_final import google_review

# %% [markdown]
# ## 處理非最終標的的情況

# %% [markdown]
# ## 使用限制

# %% [markdown]
# #### 1.僅能針對非最終標的關鍵字
# #### 2.爬取最多20個目標，即1頁
# #### 3.網頁須盡量保持半視窗且不動，不然容易中斷

# %% [markdown]
# ## 模組示範：中山區影城

# %%
google_review(search="中山區影城",scroll_time=1, review_category="最新")

# %% [markdown]
# ## 小練習
# ### 試著用模組去爬取台北商業大學 search="台北商業大學"，下滑3次 scroll_time=3，選擇最新評論

# %%
google_review("台北商業大學",3,review_category="最新")


