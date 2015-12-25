"""Change primary to unique constraint

Revision ID: 4ac191f72d8
Revises: 2baf554c632
Create Date: 2015-07-29 22:20:58.116493

"""

# revision identifiers, used by Alembic.
revision = '4ac191f72d8'
down_revision = '2baf554c632'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()





def upgrade_account():
    ### commands auto generated by Alembic - please adjust! ###
    op.execute("ALTER TABLE service_usage DROP PRIMARY KEY")
    op.execute("ALTER TABLE service_usage ADD service_usage_id INT NOT NULL AUTO_INCREMENT, ADD PRIMARY KEY(service_usage_id)")

    op.alter_column('service_usage', 'resource_id',
               existing_type=mysql.VARCHAR(length=100),
               nullable=False)
    op.create_unique_constraint(None, 'service_usage', ['tenant_id', 'service_id', 'time_label', 'resource_id'])


    ### end Alembic commands ###


def downgrade_account():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'service_usage', type_='unique')
    op.alter_column('service_usage', 'resource_id',
               existing_type=mysql.VARCHAR(length=100),
               nullable=True)
    op.drop_column('service_usage', 'service_usage_id')
    # TODO create composite primary key
    ### end Alembic commands ###


def upgrade_fitter():
    pass


def downgrade_fitter():
    pass
