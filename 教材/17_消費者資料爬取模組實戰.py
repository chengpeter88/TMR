# %% [markdown]
# # 17_消費者資料爬取模組實戰

# %% [markdown]
# ## 引入套件

# %%
from util_advance import google_review_customer

# %% [markdown]
# ## 使用限制:關鍵字需為最終標的

# %% [markdown]
# ## 以過去上課案例"臺師大"來查看結果

# %%
school,briefing=google_review_customer(search="臺大",scroll_time=4, review_category="最相關")

# %%
school.head()

# %%
briefing

# %% [markdown]
# ## 難道每次都一定要是最終標的才能操作嗎?

# %% [markdown]
# ## 小練習
# ### 試著使用模組爬取上課指定題目search="北商"、下拉5次 scroll_time=5、選擇最新評論

# %%
???
# %%
school.head()

# %%
briefing


