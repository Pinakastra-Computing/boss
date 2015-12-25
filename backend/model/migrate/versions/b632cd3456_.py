"""delete subject uniqueness

Revision ID: b632cd3456
Revises: 4cfbc4e6089
Create Date: 2015-06-17 02:33:22.441739

"""

# revision identifiers, used by Alembic.
revision = 'b632cd3456'
down_revision = '4cfbc4e6089'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()





def upgrade_account():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('subject', table_name='news')
    ### end Alembic commands ###


def downgrade_account():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_index('subject', 'news', ['subject'], unique=True)
    ### end Alembic commands ###


def upgrade_fitter():
    pass


def downgrade_fitter():
    pass

