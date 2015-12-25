"""Added foreign key for quote

Revision ID: 32879c33fd7
Revises: ec00fe423c
Create Date: 2015-11-06 16:55:07.412294

"""

# revision identifiers, used by Alembic.
revision = '32879c33fd7'
down_revision = 'ec00fe423c'
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
    op.create_foreign_key(None, 'quote', 'customer', ['customer_id'], ['customer_id'])
    ### end Alembic commands ###


def downgrade_account():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'quote', type_='foreignkey')
    ### end Alembic commands ###


def upgrade_fitter():
    pass


def downgrade_fitter():
    pass

